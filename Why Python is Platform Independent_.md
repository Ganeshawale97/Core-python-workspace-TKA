# Why Python is Platform Independent?

Python is called **platform independent** because the same Python source code can run on different operating systems without requiring major changes.

For example, the following code:

```python
print("Hello World")
```

can run on:

- Windows
- Linux
- macOS

### How does it work?

Python code is executed by a **Python interpreter**. The interpreter handles the platform-specific details.

```text
Python Source Code (.py)
          ↓
   Python Interpreter
          ↓
 ┌────────┼────────┐
 ↓        ↓        ↓
Windows  Linux    macOS
```

Therefore, developers usually do not need to write separate Python programs for each operating system.

### Example

```python
x = 10
y = 20

print(x + y)
```

The same code can produce:

```text
Output: 30
```

on Windows, Linux, and macOS.

### Important Note

Python is **mostly platform independent**, not completely platform independent. If a program uses operating-system-specific commands, libraries, or features, some changes may be required.

### Conclusion

**Python is platform independent because its interpreter allows the same Python source code to execute on multiple operating systems with little or no modification.**