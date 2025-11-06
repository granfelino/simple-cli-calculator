**Notes:**
* venv:
| Command                                              | Purpose                                 |
| ---------------------------------------------------- | --------------------------------------- |
| `python -m venv venv`                                | Create a new virtual environment        |
| `source venv/bin/activate` / `venv\Scripts\activate` | Activate the environment                |
| `pip install package`                                | Install packages inside the environment |
| `pip freeze > requirements.txt`                      | Export dependencies                     |
| `pip install -r requirements.txt`                    | Reinstall dependencies from file        |
| `deactivate`                                         | Exit the virtual environment            |


---

## **1. `venv` (Virtual Environment)**

* Creates an isolated Python environment per project.
* Keeps dependencies separate; avoids conflicts.
* Inside a venv, always use `pip` (or `python -m pip`).
* Small projects can share venvs, but per-project venvs are safest.
* Binary distributions (`.exe`, `.whl`) don’t need a venv to run.

---

## **2. Python Linting and Style**

* **Tools to check style**: `Ruff` (all-in-one), `Flake8`, `Pylint`, `Black` (formatter).
* **Ruff**: Combines linting, formatting, import sorting, docstring checks.
* **Type checking**: Use `Mypy` alongside Ruff for static type validation.

---

## **3. `pip` vs `pip3`**

* Modern systems: `pip` → Python 3.
* Virtual environments: `pip` always targets that venv’s Python.
* `pip3` may be needed on older Linux systems with Python 2 installed.
* Most robust: `python -m pip install package`.

---

## **4. Project Structure**

**Minimal professional layout:**

```
project_name/
├── README.md
├── pyproject.toml
├── requirements.txt
├── venv/
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py
│       ├── utils.py
│       └── modules/
└── tests/
    ├── test_main.py
    └── test_utils.py
```

* Keep `src/` separate from `tests/`.
* Use `__init__.py` to mark folders as packages.
* `main.py` → entry point; orchestrates logic, calls functions from modules.

---

## **5. `__init__.py`**

* Marks a folder as a package.
* Can be **empty** — imports will still work.
* Optional: expose symbols, run package-level initialization.
* Enables relative imports in subpackages.

---

## **6. Imports**

* **Relative imports** (`from .utils import foo`):

  * Only works **inside a package**.
  * Must run module with `python -m package.module` from project root.
* **Absolute imports** (`from my_package.utils import foo`):

  * More explicit, works both inside and outside the package (if package is in `PYTHONPATH`).
* Best practice: prefer absolute imports; use relative imports for deep subpackages.

---

## **7. `main.py`**

* Should define a **`main()` function**.
* Use `if __name__ == "__main__": main()` to run script safely.
* Keep actual logic in other modules; `main.py` orchestrates.
* Can handle CLI arguments, configuration, logging if needed.

---

## **8. `pyproject.toml`**

* Central configuration file for:

  * Project metadata (`[project]`): name, version, Python version, authors.
  * Build system (`[build-system]`): e.g., `requires = ["setuptools>=65", "wheel"]`, `build-backend = "setuptools.build_meta"`.
  * Tool configs (`[tool.black]`, `[tool.ruff]`, `[tool.isort]`, `[tool.mypy]`).
* Decide values based on:

  * Python version features → `requires-python`.
  * Build tools → `build-backend` and `requires`.
  * Dependencies and project complexity.

---

✅ **Big picture:**

* **Keep project modular:** `src/`, `tests/`, separate modules.
* **Use virtual environments** for isolated dependencies.
* **`__init__.py`** enables packages; imports work across files.
* **`main.py`** orchestrates logic safely.
* **Lint, format, type-check** using modern tools (Ruff + Mypy).
* **`pyproject.toml`** is your single source of truth for project config and tooling.

---
