# 🇪🇹 APL – አማርኛ Programming Language

A beginner-friendly programming language that uses **Amharic keywords** and translates source code into **Python**.

This project was developed for a **Programming Language Design** course under the theme:

> **Local Language Programming for Beginners**

The language is designed to make programming easier for Ethiopian beginners by replacing English programming keywords with understandable Amharic words.

---

# Features

## ✅ Variables

```am
ቁጥር x = 10
```

Generated Python:

```python
x = 10
```

---

## ✅ Variable Assignment

```am
x = x + 1
```

Generated Python:

```python
x = x + 1
```

---

## ✅ Arithmetic Expressions

Supported operators:

```text
+
-
*
/
```

Example:

```am
ቁጥር z = x + y
```

---

## ✅ Comparison Operators

Supported comparisons:

```text
==
<
>
```

Example:

```am
ከሆነ x > 5:
```

---

## ✅ Output (Print)

```am
ፃፍ("ሰላም")
```

Generated Python:

```python
print("ሰላም")
```

---

## ✅ If Statement

```am
ከሆነ x > 5:
ጀምር
ፃፍ("ትልቅ")
ጨርስ
```

Generated Python:

```python
if x > 5:
    print("ትልቅ")
```

---

## ✅ If / Else Statement

```am
ከሆነ x > 5:
ጀምር
ፃፍ("ትልቅ")
ጨርስ

ካልሆነ:
ጀምር
ፃፍ("ትንሽ")
ጨርስ
```

Generated Python:

```python
if x > 5:
    print("ትልቅ")
else:
    print("ትንሽ")
```

---

## ✅ While Loop

```am
ቁጥር x = 1

ሲሆን x < 5:
ጀምር
ፃፍ(x)
x = x + 1
ጨርስ
```

Generated Python:

```python
x = 1

while x < 5:
    print(x)
    x = x + 1
```

Output:

```text
1
2
3
4
```

---

## ✅ Function Definition

```am
ተግባር ድምር(a,b):
ጀምር
መልስ a + b
ጨርስ
```

Generated Python:

```python
def ድምር(a,b):
    return a + b
```

---

## ✅ Function Call

```am
ፃፍ(ድምር(3,4))
```

Output:

```text
7
```

---

## ✅ Return Values

```am
መልስ a + b
```

Generated Python:

```python
return a + b
```

---

# Language Keywords

| Amharic Keyword | Meaning              |
| --------------- | -------------------- |
| ቁጥር             | Variable declaration |
| ፃፍ              | Print                |
| ከሆነ             | If                   |
| ካልሆነ            | Else                 |
| ሲሆን             | While                |
| ተግባር            | Function             |
| መልስ             | Return               |
| ጀምር             | Begin block          |
| ጨርስ             | End block            |

---

# Beginner-Friendly Design

The language uses explicit block delimiters:

```am
ጀምር
...
ጨርስ
```

instead of indentation-based syntax.

Benefits:

- Easier for beginners
- Clear program structure
- Fewer indentation mistakes
- Simpler parser implementation
- More readable code

Example:

```am
ከሆነ x > 5:
ጀምር
ፃፍ("OK")
ጨርስ
```

---

# Source File Extension

APL source files use the extension:

```text
.አም
```

Example:

```text
program.አም
```

Generated output:

```text
program.py
```

---

# Project Structure

```text
APL/
│
├── lexer.py
├── parser.py
├── nodes.py
├── codegen.py
├── translator.py
│
├── README.md
│
└── examples/
    ├── basic.አም
    ├── control.አም
    ├── function.አም
```

---

# Compiler Architecture

The translator consists of three major stages:

## 1. Lexer

The lexer:

- Reads source code
- Handles Unicode Amharic text
- Recognizes keywords
- Produces tokens

Example:

```am
ቁጥር x = 10
```

Tokens:

```python
[
 ('VAR','ቁጥር'),
 ('ID','x'),
 ('ASSIGN','='),
 ('NUMBER','10')
]
```

---

## 2. Parser

The parser:

- Reads tokens
- Validates syntax
- Builds an Abstract Syntax Tree (AST)

Example AST:

```python
VarAssign(
    "x",
    Number("10")
)
```

---

## 3. Code Generator

The code generator:

- Traverses the AST
- Produces valid Python source code

Example:

AST:

```python
Print(Number("5"))
```

Generated:

```python
print(5)
```

---

# Installation

Requirements:

```text
Python 3.10+
```

Clone the project:

```bash
git clone <repository-url>
cd APL
```

---

# Usage

Translate an Amharic source file:

```bash
python3 translator.py examples/basic.አም
```

Output:

```text
✅ ተተርጎሟል: examples/basic.py
```

Run the generated Python file:

```bash
python3 examples/basic.py
```

---

# Example Program

Source file:

```am
ተግባር ድምር(a,b):
ጀምር
መልስ a + b
ጨርስ

ቁጥር x = 10

ከሆነ x > 5:
ጀምር
ፃፍ("ትልቅ")
ጨርስ

ፃፍ(ድምር(3,4))
```

Generated Python:

```python
def ድምር(a,b):
    return a + b

x = 10

if x > 5:
    print("ትልቅ")

print(ድምር(3,4))
```

Output:

```text
ትልቅ
7
```

---

# Project Requirements Coverage

| Requirement                  | Status |
| ---------------------------- | ------ |
| Variables                    | ✅     |
| Assignment                   | ✅     |
| Arithmetic Expressions       | ✅     |
| Comparisons                  | ✅     |
| If / Else                    | ✅     |
| While Loop                   | ✅     |
| Functions                    | ✅     |
| Function Calls               | ✅     |
| Return Values                | ✅     |
| Unicode Support              | ✅     |
| Lexer                        | ✅     |
| Parser                       | ✅     |
| AST Construction             | ✅     |
| Source-to-Source Translation | ✅     |
| Beginner-Friendly Feature    | ✅     |
| Valid Python Output          | ✅     |

---

# Design Decisions

1. Amharic keywords were chosen to improve accessibility for beginners.
2. Explicit block markers (`ጀምር` / `ጨርስ`) were used instead of indentation.
3. Python was selected as the target language because of its readability.
4. The compiler uses an AST rather than simple text replacement.
5. Full Unicode support allows Amharic identifiers and keywords.

---

# Language Information

**Language Name:** APL (Amharic Programming Language)

**Source Extension:** `.አም`

**Target Language:** Python

**Translation Type:** Source-to-Source Compiler

**Course:** Programming Language Design

**Project Theme:** Local Language Programming for Beginners

---

# License

This project is intended for educational and academic purposes.
