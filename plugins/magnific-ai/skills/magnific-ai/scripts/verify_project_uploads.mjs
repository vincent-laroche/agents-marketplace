#!/usr/bin/env node

import { spawn } from "node:child_process";
import { readFile } from "node:fs/promises";
import path from "node:path";

const ROOT = path.resolve(import.meta.dirname, "..");

function usage() {
  return [
    "Usage:",
    "  node scripts/verify_project_uploads.mjs \\",
    '    --project-name "Project Name" \\',
    "    --manifest /absolute/path/to/manifest.json \\",
    "    [--assets-key assets] [--path-field local_path]",
  ].join("\n");
}

function parseArgs(argv) {
  const options = { assetsKey: "assets", pathField: "local_path" };
  for (let index = 0; index < argv.length; index += 2) {
    const flag = argv[index];
    const value = argv[index + 1];
    if (!value) throw new Error(`Missing value for ${flag}\n\n${usage()}`);
    if (flag === "--project-name") options.projectName = value;
    else if (flag === "--manifest") options.manifest = path.resolve(value);
    else if (flag === "--assets-key") options.assetsKey = value;
    else if (flag === "--path-field") options.pathField = value;
    else throw new Error(`Unknown argument: ${flag}\n\n${usage()}`);
  }
  if (!options.projectName || !options.manifest) throw new Error(usage());
  return options;
}

function frequencies(values) {
  const result = new Map();
  for (const value of values) result.set(value, (result.get(value) ?? 0) + 1);
  return result;
}

function compareMultisets(expected, actual) {
  const expectedCounts = frequencies(expected);
  const actualCounts = frequencies(actual);
  const names = new Set([...expectedCounts.keys(), ...actualCounts.keys()]);
  const missing = [];
  const unexpected = [];

  for (const name of names) {
    const wanted = expectedCounts.get(name) ?? 0;
    const found = actualCounts.get(name) ?? 0;
    if (found < wanted) missing.push({ name, count: wanted - found });
    if (found > wanted) unexpected.push({ name, count: found - wanted });
  }

  return {
    missing,
    unexpected,
    duplicateNames: [...actualCounts.entries()]
      .filter(([, count]) => count > 1)
      .map(([name, count]) => ({ name, count })),
  };
}

function contentText(result) {
  const text = result?.content?.find((item) => item.type === "text")?.text;
  if (!text) throw new Error("Magnific returned no text content.");
  if (result.isError) throw new Error("Magnific returned a transient read error.");
  return text;
}

function parseProjects(text) {
  const projects = [];
  const matcher = /^\s*-\s+reference:\s*(.+)\n\s+name:\s*(.+)$/gm;
  for (const match of text.matchAll(matcher)) {
    projects.push({ reference: match[1].trim(), name: match[2].trim() });
  }
  return projects;
}

function parseSearch(text) {
  const total = Number(text.match(/^\s*total:\s*(\d+)$/m)?.[1]);
  const lastPage = Number(text.match(/^\s*lastPage:\s*(\d+)$/m)?.[1]);
  const prompts = [];

  for (const line of text.split("\n")) {
    const match = line.match(/^\s{2}[^,]+,(.*),upload$/);
    if (match) prompts.push(match[1]);
  }

  if (!Number.isFinite(total) || !Number.isFinite(lastPage)) {
    throw new Error("Magnific pagination metadata was missing.");
  }
  return { total, lastPage, prompts };
}

function delay(milliseconds) {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
}

async function readWithRetries(operation) {
  let lastError;
  for (let attempt = 1; attempt <= 4; attempt++) {
    try {
      return await operation();
    } catch (error) {
      lastError = error;
      if (attempt < 4) await delay(750 * attempt);
    }
  }
  throw lastError;
}

class McpClient {
  constructor() {
    this.nextId = 1;
    this.pending = new Map();
    this.buffer = "";
    this.child = spawn("npx", ["-y", "mcp-remote", "https://mcp.magnific.com"], {
      cwd: ROOT,
      stdio: ["pipe", "pipe", "ignore"],
    });

    this.child.stdout.setEncoding("utf8");
    this.child.stdout.on("data", (chunk) => {
      this.buffer += chunk;
      let newline;
      while ((newline = this.buffer.indexOf("\n")) >= 0) {
        const line = this.buffer.slice(0, newline).trim();
        this.buffer = this.buffer.slice(newline + 1);
        if (!line.startsWith("{")) continue;
        const message = JSON.parse(line);
        if (message.id == null) continue;
        const pending = this.pending.get(message.id);
        if (!pending) continue;
        this.pending.delete(message.id);
        clearTimeout(pending.timer);
        if (message.error) pending.reject(new Error(message.error.message));
        else pending.resolve(message.result);
      }
    });
  }

  request(method, params) {
    const id = this.nextId++;
    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`Timed out waiting for ${method}.`));
      }, 30_000);
      this.pending.set(id, { resolve, reject, timer });
      this.child.stdin.write(`${JSON.stringify({ jsonrpc: "2.0", id, method, params })}\n`);
    });
  }

  notify(method, params = {}) {
    this.child.stdin.write(`${JSON.stringify({ jsonrpc: "2.0", method, params })}\n`);
  }

  async start() {
    await this.request("initialize", {
      protocolVersion: "2025-03-26",
      capabilities: {},
      clientInfo: { name: "magnific-project-verifier", version: "1.0.0" },
    });
    this.notify("notifications/initialized");
  }

  callTool(name, args) {
    return this.request("tools/call", { name, arguments: args });
  }

  close() {
    this.child.kill("SIGTERM");
  }
}

const options = parseArgs(process.argv.slice(2));
const manifest = JSON.parse(await readFile(options.manifest, "utf8"));
const assets = manifest[options.assetsKey];
if (!Array.isArray(assets)) {
  throw new Error(`Manifest field "${options.assetsKey}" must be an array.`);
}

const expected = assets.map((asset, index) => {
  const filePath = asset?.[options.pathField];
  if (typeof filePath !== "string" || !filePath) {
    throw new Error(`Asset ${index} has no string "${options.pathField}" value.`);
  }
  return path.basename(filePath, path.extname(filePath));
});

const client = new McpClient();

try {
  await client.start();
  const projectText = contentText(
    await readWithRetries(() => client.callTool("folders_list", { onlyProjects: true })),
  );
  const matches = parseProjects(projectText).filter(
    (project) => project.name === options.projectName,
  );
  if (matches.length !== 1) {
    throw new Error(
      `Expected exactly one project named "${options.projectName}", found ${matches.length}.`,
    );
  }

  const project = matches[0];
  const first = await readWithRetries(async () =>
    parseSearch(
      contentText(
        await client.callTool("creations_search", {
          from: "project-root",
          reference: project.reference,
          page: 1,
          perPage: 50,
          orderBy: "created_at",
          orderDirection: "asc",
        }),
      ),
    ),
  );

  const actual = [...first.prompts];
  for (let pageNumber = 2; pageNumber <= first.lastPage; pageNumber++) {
    const next = await readWithRetries(async () =>
      parseSearch(
        contentText(
          await client.callTool("creations_search", {
            from: "project-root",
            reference: project.reference,
            page: pageNumber,
            perPage: 50,
            orderBy: "created_at",
            orderDirection: "asc",
          }),
        ),
      ),
    );
    actual.push(...next.prompts);
  }

  const comparison = compareMultisets(expected, actual);
  const result = {
    project: options.projectName,
    manifestCount: expected.length,
    magnificCount: first.total,
    fetchedCount: actual.length,
    ...comparison,
  };
  result.verified =
    result.manifestCount === result.magnificCount &&
    result.magnificCount === result.fetchedCount &&
    result.missing.length === 0 &&
    result.unexpected.length === 0 &&
    result.duplicateNames.length === 0;

  console.log(JSON.stringify(result, null, 2));
  if (!result.verified) process.exitCode = 1;
} finally {
  client.close();
}
