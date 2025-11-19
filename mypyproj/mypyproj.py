import argparse
from pathlib import Path

TEMPLATE = {
    "pyproject": """\
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "{version}"
description = "{description}"
requires-python = "{python}"
readme = "README.md"
license = {{ text = "MIT" }}
authors = [ {{ name = "{author}" }} ]

dependencies = []

[project.optional-dependencies]
dev = ["pytest"]

[tool.setuptools.packages.find]
where = ["src"]
""",

    "readme": """\
# {project_name}

{description}

## Install
pip install -e ".[dev]"

## Test
pytest
""",

    "gitignore": """\
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.venv/
venv/
""",

    "init": """\
from .version import __version__
__all__ = ["__version__"]
""",

    "version": """\
__version__ = "{version}"
""",

    "test": """\
from {pkg} import __version__

def test_version():
    assert isinstance(__version__, str)
"""
}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("name", help="Project path (can be just a name or a full path).")
    p.add_argument("--author", default="Your Name")
    p.add_argument("--version", default="0.1.0")
    p.add_argument("--python", default=">=3.10")
    p.add_argument("--description", default="A minimal Python project.")
    args = p.parse_args()

    # Expand ~ and handle full paths
    root = Path(args.name).expanduser()
    project_name = root.name          # last part of the path
    pkg = project_name.replace("-", "_")

    # --- Clean up legacy files from older script versions (optional but handy) ---
    for legacy in ["version.py", "__init__.py"]:
        legacy_path = root / legacy
        if legacy_path.exists():
            legacy_path.unlink()

    # --- Create directory structure ---
    (root / "src" / pkg).mkdir(parents=True, exist_ok=True)
    (root / "tests").mkdir(parents=True, exist_ok=True)
    (root / "scripts").mkdir(parents=True, exist_ok=True)  # <--- new scripts folder

    # --- pyproject.toml ---
    (root / "pyproject.toml").write_text(
        TEMPLATE["pyproject"].format(
            project_name=project_name,
            version=args.version,
            author=args.author,
            description=args.description,
            python=args.python,
        )
    )

    # --- README.md ---
    (root / "README.md").write_text(
        TEMPLATE["readme"].format(
            project_name=project_name,
            description=args.description,
        )
    )

    # --- .gitignore ---
    (root / ".gitignore").write_text(TEMPLATE["gitignore"])

    # --- src/<pkg>/__init__.py ---
    (root / "src" / pkg / "__init__.py").write_text(TEMPLATE["init"])

    # --- src/<pkg>/version.py ---
    (root / "src" / pkg / "version.py").write_text(
        TEMPLATE["version"].format(version=args.version)
    )

    # --- tests/test_basic.py ---
    (root / "tests" / "test_basic.py").write_text(
        TEMPLATE["test"].format(pkg=pkg)
    )

    print(f"\nProject created at: {root}/")
    print("Run:")
    print(f"  cd {root}")
    print('  pip install -e ".[dev]"')


if __name__ == "__main__":
    main()

