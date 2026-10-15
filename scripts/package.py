"""Build the plugin ZIP or synchronize its release version."""

import argparse
import json
from pathlib import Path
import re
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ("plugin.json", ".claude-plugin/plugin.json")


def version_tuple(value):
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", value):
        raise ValueError("Use a stable numeric version: X.Y.Z (without a v prefix).")
    return tuple(map(int, value.split(".")))


def manifests(root):
    return [json.loads((root / path).read_text()) for path in MANIFESTS]


def set_version(root, version):
    requested = version_tuple(version)
    current = manifests(root)
    if any(requested < version_tuple(item["version"]) for item in current):
        raise ValueError("A release cannot decrease either manifest version.")
    for path, item in zip(MANIFESTS, current):
        if item["version"] != version:
            item["version"] = version
            (root / path).write_text(json.dumps(item, indent=2) + "\n")


def build(root, output):
    portable, claude = manifests(root)
    version_tuple(portable["version"])
    if (portable["name"], portable["version"]) != (claude["name"], claude["version"]):
        raise ValueError("Plugin names and versions must match before packaging.")
    skills = root / "skills"
    if output.resolve().is_relative_to(root.resolve()):
        raise ValueError("Write the archive outside the plugin repository.")
    paths = [root / path for path in (*MANIFESTS, "LICENSE")]
    paths += sorted(skills.rglob("*"))
    if not any(path.name == "SKILL.md" for path in paths):
        raise ValueError("No skills found.")
    if (any(path.is_symlink() or not path.resolve().is_relative_to(root.resolve())
            for path in paths) or skills.is_symlink()):
        raise ValueError("Package files and directories must not be symlinks.")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=output.parent, delete=False) as handle:
        temporary = Path(handle.name)
    try:
        with ZipFile(temporary, "w") as archive:
            for path in paths:
                if path.is_file():
                    info = ZipInfo(path.relative_to(root).as_posix())
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes(), compress_type=ZIP_DEFLATED)
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build").add_argument("--output", type=Path, required=True)
    commands.add_parser("version").add_argument("version")
    args = parser.parse_args()
    try:
        if args.command == "build":
            build(ROOT, args.output)
        else:
            set_version(ROOT, args.version)
    except (ValueError, OSError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
