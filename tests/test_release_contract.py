from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "check-release.py"


class ReleaseContractTests(unittest.TestCase):
    def run_check(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(root)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_release_check_requires_semver_root_and_plugin_versions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "plugins" / "sample" / ".codex-plugin" / "plugin.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(json.dumps({"name": "sample", "version": "1.2.3"}), encoding="utf-8")
            (root / "VERSION").write_text("not-semver\n", encoding="utf-8")
            invalid = self.run_check(root)
            self.assertEqual(invalid.returncode, 1)
            self.assertIn("VERSION", invalid.stdout + invalid.stderr)

            (root / "VERSION").write_text("1.0.0\n", encoding="utf-8")
            valid = self.run_check(root)
            self.assertEqual(valid.returncode, 0, valid.stdout + valid.stderr)


if __name__ == "__main__":
    unittest.main()
