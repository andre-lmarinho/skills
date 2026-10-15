"""Check release packaging and versioning in a disposable copy."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from zipfile import ZipFile

from package import ROOT, MANIFESTS, build, manifests, set_version


class PackageTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "plugin"
        self.root.mkdir()
        for name in ("plugin.json", "LICENSE"):
            shutil.copy2(ROOT / name, self.root / name)
        shutil.copytree(ROOT / ".claude-plugin", self.root / ".claude-plugin")
        shutil.copytree(ROOT / "skills", self.root / "skills")

    def test_archive_is_complete_and_excludes_repository_files(self):
        (self.root / ".env").write_text("DO_NOT_PACKAGE=1")
        output = self.root.parent / "plugin.zip"
        before = manifests(self.root)
        with redirect_stdout(io.StringIO()):
            build(self.root, output)
        with ZipFile(output) as archive:
            expected = set(MANIFESTS) | {"LICENSE"}
            expected |= {path.relative_to(self.root).as_posix()
                         for path in (self.root / "skills").rglob("*") if path.is_file()}
            self.assertEqual(set(archive.namelist()), expected)
            for name in expected:
                self.assertEqual(archive.read(name), (self.root / name).read_bytes())
        self.assertEqual(manifests(self.root), before)

    def test_versions_change_together_and_invalid_input_does_not_write(self):
        current = manifests(self.root)[0]["version"]
        major = int(current.split(".")[0]) + 1
        version = f"{major}.0.0"
        set_version(self.root, version)
        self.assertEqual([item["version"] for item in manifests(self.root)], [version] * 2)
        before = [(self.root / name).read_bytes() for name in MANIFESTS]
        for invalid in (current, "v1.0.0", "01.0.0", "1.0.0-beta", "1.0.0\nanything"):
            with self.subTest(version=invalid), self.assertRaises(ValueError):
                set_version(self.root, invalid)
        self.assertEqual([(self.root / name).read_bytes() for name in MANIFESTS], before)
        set_version(self.root, version)
        self.assertEqual([(self.root / name).read_bytes() for name in MANIFESTS], before)

    def test_mismatch_and_symlinks_do_not_create_an_archive(self):
        output = self.root.parent / "plugin.zip"
        manifest = self.root / MANIFESTS[1]
        data = json.loads(manifest.read_text())
        data["version"] = "999.0.0"
        manifest.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            build(self.root, output)
        self.assertFalse(output.exists())
        set_version(self.root, "999.0.0")
        (self.root / "skills" / "outside").symlink_to(self.root / "LICENSE")
        with self.assertRaises(ValueError):
            build(self.root, output)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
