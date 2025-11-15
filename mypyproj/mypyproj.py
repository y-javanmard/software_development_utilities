import argparse
from pathlib import Path

TEMPLATE = {
"pyproject": """\
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "{name}"
version = "{version}"
description = "{description}"
requires-python = "{python}"
readme = "README.md"
license = { text = "MIT" }
authors = [ { name = "{author}" } ]

dependencies = []

[project.optional-dependencies]
dev = ["pytest"]

[tool.setuptools.packages.find]
where = ["src"]
""",

"readme": """\
# {name}

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
    p.add_argument("name")
    p.add_argument("--author", default="Your Name")
    p.add_argument("--version", default="0.1.0")
    p.add_argument("--python", default=">=3.10")
    p.add_argument("--description", default="A minimal Python project.")
    args = p.parse_args()

    root = Path(args.name)
    pkg = args.name.replace("-", "_")

    (root / "src" / pkg).mkdir(parents=True)
    (root / "tests").mkdir()

    (root / "pyproject.toml").write_text(
        TEMPLATE["pyproject"].format(
            name=args.name,
            version=args.version,
            author=args.author,
            description=args.description,
            python=args.python,
        )
    )

    (root / "README.md").write_text(
        TEMPLATE["readme"].format(
            name=args.name,
            description=args.description
        )
    )

    (root / ".gitignore").write_text(TEMPLATE["gitignore"])
    (root / f"src/{pkg}/__init__.py").write_text(TEMPLATE["init"])
    (root / f"src/{pkg}/version.py").write_text(
        TEMPLATE["version"].format(version=args.version)
    )

    (root / "tests/test_basic.py").write_text(
        TEMPLATE["test"].format(pkg=pkg)
    )

    print(f"\nProject created at: {root}/")
    print("Run:")
    print(f"  cd {root}")
    print('  pip install -e ".[dev]"')


if __name__ == "__main__":
    main()
