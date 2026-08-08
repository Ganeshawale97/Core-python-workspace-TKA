# How Python Works Internally

Python is a **high-level, interpreted programming language**, but internally it uses several steps to execute a program.

### 1. Python Source Code
We first write Python code in a `.py` file.

```python
x = 10
print(x)
```

### 2. Lexical Analysis
Python reads the source code and breaks it into **tokens** such as keywords, identifiers, operators, and literals.

For example:

```python
x = 10
```

is divided into tokens like `x`, `=`, and `10`.

### 3. Parsing
Python checks the syntax of the code and builds an internal structure called an **Abstract Syntax Tree (AST)**.

If the syntax is incorrect, Python raises a `SyntaxError`.

### 4. Bytecode Compilation
The Python source code is compiled into **bytecode**.

Bytecode is an intermediate, platform-independent set of instructions. It is often stored in `.pyc` files inside the `__pycache__` directory.

Example:

```text
.py file
   ↓
Bytecode
   ↓
.pyc file (when applicable)
```

### 5. Python Virtual Machine (PVM)
The **Python Virtual Machine (PVM)** executes the bytecode instruction by instruction.

The PVM is the main component responsible for running Python bytecode.

```text
Python Code (.py)
       ↓
   Tokenization
       ↓
     Parsing
       ↓
  Compilation
       ↓
    Bytecode
       ↓
      PVM
       ↓
     Output
```

### 6. Memory Management
Python automatically manages memory using mechanisms such as:

- **Reference counting**
- **Garbage collection**
- **Private heap**
- **Memory allocators**

For example:

```python
a = 10
b = a
```

Both `a` and `b` can refer to the same integer object in memory.

### 7. Python Interpreter
The term **Python interpreter** generally refers to the implementation that reads/executes Python programs. The most widely used implementation is **CPython**.

Other implementations include **PyPy**, **Jython**, and **IronPython**.

## Simple Summary

Python internally works approximately like this:

**Source Code → Tokens → AST → Bytecode → Python Virtual Machine → Machine-level operations → Output**

This process allows Python to provide a simple programming experience while handling compilation, execution, and memory management internally.