"""Validate skills and manifests with their upstream validators."""

import argparse
import json
from pathlib import Path
import subprocess
import sys

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    args = parser.parse_args()
    schema = json.loads(args.schema.read_text())
    Draft202012Validator.check_schema(schema)
    portable = json.loads((ROOT / "plugin.json").read_text())
    Draft202012Validator(schema).validate(portable)
    claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    for field in ("name", "version", "description", "author", "repository", "license"):
        if portable[field] != claude[field]:
            parser.exit(1, f"Manifest field differs: {field}\n")
    skills = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    if not skills:
        parser.exit(1, "No skill directories found.\n")
    for skill in skills:
        subprocess.run([sys.executable, "-m", "skills_ref.cli", "validate", str(skill)], check=True)
    subprocess.run(["claude", "plugin", "validate", str(ROOT / ".claude-plugin/plugin.json"),
                    "--strict"], check=True)
    subprocess.run(["claude", "plugin", "validate", str(ROOT / ".claude-plugin/marketplace.json"),
                    "--strict"], check=True)
    print("Skills and plugin manifests validated.")


if __name__ == "__main__":
    main()
