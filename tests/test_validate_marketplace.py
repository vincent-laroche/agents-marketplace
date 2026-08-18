from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "validate-marketplace.py"
SPEC = importlib.util.spec_from_file_location("marketplace_validator", SCRIPT)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class MarketplaceValidatorTests(unittest.TestCase):
    def test_skill_description_has_a_discovery_budget(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills" / "verbose"
            skill.mkdir(parents=True)
            skill_file = skill / "SKILL.md"
            skill_file.write_text(
                f"---\nname: verbose\ndescription: {'x' * 221}\n---\n\n# Verbose\n",
                encoding="utf-8",
            )
            errors: list[str] = []
            validator.validate_skill(skill, errors, root=root)
            self.assertTrue(any("220 characters" in error for error in errors), errors)

    def test_native_codex_hook_manifest_is_validated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            plugin = Path(directory)
            hook = plugin / "hooks" / "hooks.json"
            script = plugin / "scripts" / "check.py"
            hook.parent.mkdir(parents=True)
            script.parent.mkdir(parents=True)
            script.write_text("print('ok')\n", encoding="utf-8")
            hook.write_text(
                json.dumps(
                    {
                        "hooks": {
                            "SessionStart": [
                                {
                                    "hooks": [
                                        {
                                            "type": "command",
                                            "command": "python3 ${PLUGIN_ROOT}/scripts/check.py",
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ),
                encoding="utf-8",
            )
            errors: list[str] = []
            validator.validate_hooks(plugin, "./hooks/hooks.json", errors, root=plugin)
            self.assertEqual(errors, [])

            hook.write_text(hook.read_text(encoding="utf-8").replace("${PLUGIN_ROOT}", "/Users/example"), encoding="utf-8")
            validator.validate_hooks(plugin, "./hooks/hooks.json", errors := [], root=plugin)
            self.assertTrue(any("portable" in error or "PLUGIN_ROOT" in error for error in errors), errors)

    def test_selection_evals_require_direct_indirect_and_negative_prompts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evals = root / "evals" / "plugin-selection.json"
            evals.parent.mkdir(parents=True)
            evals.write_text(
                json.dumps(
                    {
                        "plugins": {
                            "sample": {
                                "direct": ["Use sample."],
                                "indirect": ["Review this artifact."],
                                "negative": [],
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            errors: list[str] = []
            validator.validate_selection_evals(evals, {"sample"}, errors, root=root)
            self.assertTrue(any("negative" in error for error in errors), errors)

    def test_agent_requires_explicit_model_tier(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            agent = root / "agent.toml"
            agent.write_text(
                'name = "Reviewer"\ndescription = "Reviews."\ndeveloper_instructions = "Review."\nsandbox_mode = "read-only"\n',
                encoding="utf-8",
            )
            errors: list[str] = []
            validator.validate_agent(agent, set(), errors, root=root)
            self.assertTrue(any("model" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
