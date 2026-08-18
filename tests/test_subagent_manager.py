from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "install-subagents.py"


def write_marketplace(root: Path, *, installation: str = "INSTALLED_BY_DEFAULT") -> Path:
    plugin = root / "plugins" / "sample"
    agents = plugin / "agents"
    agents.mkdir(parents=True, exist_ok=True)
    (agents / "reviewer.toml").write_text(
        '\n'.join(
            (
                'name = "Sample Reviewer"',
                'description = "Reviews sample work."',
                'model = "gpt-5.6-terra"',
                'model_reasoning_effort = "medium"',
                'sandbox_mode = "read-only"',
                'developer_instructions = "Review the supplied work."',
                "",
            )
        ),
        encoding="utf-8",
    )
    catalog = root / ".agents" / "plugins" / "marketplace.json"
    catalog.parent.mkdir(parents=True, exist_ok=True)
    catalog.write_text(
        json.dumps(
            {
                "name": "agents-marketplace",
                "plugins": [
                    {
                        "name": "sample",
                        "source": {"source": "local", "path": "./plugins/sample"},
                        "policy": {"installation": installation, "authentication": "ON_USE"},
                        "category": "Testing",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return agents / "reviewer.toml"


class SubagentManagerTests(unittest.TestCase):
    def run_manager(self, root: Path, codex_home: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                *arguments,
                "--root",
                str(root),
                "--codex-home",
                str(codex_home),
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_managed_lifecycle_install_update_status_prune_and_uninstall(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "marketplace"
            codex_home = base / "codex"
            source = write_marketplace(root)

            installed = self.run_manager(root, codex_home, "install")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            target = codex_home / "agents" / "sample-reviewer.toml"
            state = codex_home / "agents" / ".agents-marketplace-state.json"
            self.assertTrue(target.is_file())
            self.assertTrue(state.is_file())
            self.assertIn("Sample Reviewer", state.read_text(encoding="utf-8"))

            current = self.run_manager(root, codex_home, "status")
            self.assertEqual(current.returncode, 0, current.stdout + current.stderr)

            source.write_text(source.read_text(encoding="utf-8").replace("Reviews sample", "Audits sample"), encoding="utf-8")
            drift = self.run_manager(root, codex_home, "status")
            self.assertEqual(drift.returncode, 1)
            self.assertIn("drift", drift.stdout.lower())

            updated = self.run_manager(root, codex_home, "update")
            self.assertEqual(updated.returncode, 0, updated.stderr)
            self.assertIn("Audits sample", target.read_text(encoding="utf-8"))

            source.unlink()
            pruned = self.run_manager(root, codex_home, "prune")
            self.assertEqual(pruned.returncode, 0, pruned.stderr)
            self.assertFalse(target.exists())
            self.assertTrue((codex_home / "agents" / ".agents-marketplace-trash").is_dir())

            write_marketplace(root)
            self.assertEqual(self.run_manager(root, codex_home, "install").returncode, 0)
            removed = self.run_manager(root, codex_home, "uninstall")
            self.assertEqual(removed.returncode, 0, removed.stderr)
            self.assertFalse(target.exists())

    def test_install_refuses_unmanaged_same_name_agent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "marketplace"
            codex_home = base / "codex"
            write_marketplace(root)
            registry = codex_home / "agents"
            registry.mkdir(parents=True)
            unmanaged = registry / "personal-reviewer.toml"
            unmanaged.write_text(
                'name = "Sample Reviewer"\ndescription = "Personal."\ndeveloper_instructions = "Personal."\nsandbox_mode = "read-only"\n',
                encoding="utf-8",
            )

            result = self.run_manager(root, codex_home, "install")
            self.assertEqual(result.returncode, 1)
            self.assertIn("unmanaged", (result.stdout + result.stderr).lower())
            self.assertEqual(unmanaged.read_text(encoding="utf-8").splitlines()[1], 'description = "Personal."')

            adopted = self.run_manager(root, codex_home, "install", "--adopt-existing")
            self.assertEqual(adopted.returncode, 0, adopted.stderr)
            self.assertFalse(unmanaged.exists())
            self.assertTrue((registry / "sample-reviewer.toml").is_file())
            registered = list(registry.glob("*.toml"))
            self.assertEqual(len(registered), 1)
            self.assertTrue((registry / ".agents-marketplace-trash").is_dir())

    def test_available_plugin_requires_explicit_selection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root = base / "marketplace"
            codex_home = base / "codex"
            write_marketplace(root, installation="AVAILABLE")

            default = self.run_manager(root, codex_home, "install")
            self.assertEqual(default.returncode, 0, default.stderr)
            self.assertFalse((codex_home / "agents" / "sample-reviewer.toml").exists())

            selected = self.run_manager(root, codex_home, "install", "--plugin", "sample")
            self.assertEqual(selected.returncode, 0, selected.stderr)
            self.assertTrue((codex_home / "agents" / "sample-reviewer.toml").exists())


if __name__ == "__main__":
    unittest.main()
