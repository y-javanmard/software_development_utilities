## ⭐ HOW TO USE IT

You can generate a brand-new minimal Python project anywhere on your machine.

### 📌 Example

```bash
python mkpyproj/mkpyproj.py myproject \
    --author "Younes Javanmard" \
    --python ">=3.11" \
    --version "0.0.1"
```

### It creates:

```
myproject/
    pyproject.toml
    README.md
    .gitignore
    src/
        myproject/
            __init__.py
            version.py
    tests/
        test_basic.py

```
### One can navigate:
```
cd myproject
pip install -e ".[dev]"
pytest
```

and this is the structure of the project:

```
myproject/
    pyproject.toml
    README.md
    .gitignore
    src/
        myproject/
            __init__.py
            version.py
    tests/
        test_basic.py

```

### Options:

```
python mkpyproj.py --help
```

