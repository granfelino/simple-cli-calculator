## 🧭 **Project Title: Simple CLI Calculator**

### **Objective**

Build a **command-line interface (CLI) calculator** in Python that accepts input arguments, performs basic arithmetic operations, and returns results in a user-friendly format.
This project will reinforce your understanding of:

* Python syntax and structure
* Argument parsing with `argparse`
* Functions and control flow
* Error handling and Pythonic conventions

---

## 🧩 **Functional Requirements**

### **1. Basic Operations**

The calculator should support:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* (Optional advanced stretch goals) Power (`^`), Modulus (`%`)

Example:

```bash
$ python calculator.py add 5 3
Result: 8
```

---

### **2. Multiple Inputs**

* The program should accept **two or more operands** (e.g., `add 2 3 4` → `9`).
* Ensure calculations handle any number of numeric arguments gracefully.

---

### **3. Command-Line Interface (CLI)**

Use Python’s built-in **`argparse`** module to:

* Parse operation type (`add`, `sub`, `mul`, `div`)
* Parse numeric values as arguments
* Display help messages and usage instructions

Example:

```bash
$ python calculator.py --help
usage: calculator.py [operation] [numbers...]
Supported operations: add, sub, mul, div
Example: python calculator.py add 2 3 4
```

---

### **4. Error Handling**

The program must:

* Handle **invalid operations** (e.g., `python calculator.py sqrt 4`)
* Handle **non-numeric inputs**
* Gracefully handle **division by zero**
* Display **user-friendly error messages** without crashing

Example:

```bash
$ python calculator.py div 10 0
Error: Division by zero is not allowed.
```

---

### **5. Output Formatting**

* Print results in a **clean, consistent format**, e.g.:

  ```
  Operation: add
  Numbers: [2, 3, 4]
  Result: 9
  ```
* Optionally support a **verbose flag** (`--verbose`) to show step-by-step calculations:

  ```
  2 + 3 + 4 = 9
  ```

---

## ⚙️ **Technical Requirements**

| Category                    | Requirement                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------- |
| **Python Version**          | 3.8+                                                                               |
| **Modules Used**            | `argparse`, `sys` (optional), `math` (optional for extra functions)                |
| **Development Environment** | VSCode or PyCharm                                                                  |
| **Virtual Environment**     | Required (`python -m venv venv`)                                                   |
| **Style Guidelines**        | Follow PEP8 (Python standard style guide)                                          |
| **Comments & Docstrings**   | Each function should include a concise docstring explaining purpose and parameters |

---

## 🧠 **Concepts Reinforced**

| Concept                           | Application                                  |
| --------------------------------- | -------------------------------------------- |
| **Variables & Data Types**        | Store operation names and operands           |
| **Conditionals**                  | Select operation type                        |
| **Loops**                         | Iterate over multiple numbers                |
| **Functions**                     | Encapsulate each operation                   |
| **Error Handling (`try/except`)** | Manage invalid inputs                        |
| **List Comprehensions**           | Convert input strings to numbers             |
| **Argument Parsing (`argparse`)** | Build CLI                                    |
| **Unpacking**                     | Pass lists of numbers to functions (`*args`) |

---

## 🚀 **Stretch Goals (Optional Enhancements)**

If you complete the basics early:

1. **Add advanced operations** — square root, exponentiation, factorial.
2. **Add unit tests** using `unittest` or `pytest`.
3. **Add colorized output** using `colorama`.
4. **Add interactive mode** — if no arguments are given, enter an input loop.
5. **Add logging** to record calculations to a file (`calculator.log`).

---

## 📅 **Weekly Milestones**

| Day       | Focus                                  | Deliverable                  |
| --------- | -------------------------------------- | ---------------------------- |
| **Day 1** | Set up Python, venv, and IDE           | Working environment          |
| **Day 2** | Learn basics: syntax, variables, loops | Practice scripts             |
| **Day 3** | Learn functions and conditionals       | Simple arithmetic functions  |
| **Day 4** | Learn and test `argparse`              | Parse example arguments      |
| **Day 5** | Build basic CLI calculator             | Basic arithmetic works       |
| **Day 6** | Add error handling, formatting         | Clean output & validations   |
| **Day 7** | Polish and test                        | Final working CLI calculator |

---
