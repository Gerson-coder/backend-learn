# Code Context

## Files Retrieved
1. `niveles.md` (lines 1-91) - master exercise roadmap from beginner Python fundamentals through files and comprehensions.
2. `notas/01-def-main-y-if-name-main.md` (lines 1-200) - teaching note explaining professional script structure with `main()` and the `__name__` guard.
3. `nivel-1/nivel1.py` (lines 1-15) - Celsius-to-Fahrenheit exercise.
4. `nivel-1/nivel1.2.py` (lines 1-16) - age calculation exercise.
5. `nivel-1/nivel1.3.py` (lines 1-23) - variable swap exercise.
6. `nivel-2/nivel2.1.py` (lines 1-19) - even/odd exercise using modulo.
7. `nivel-2/nivel2.2.py` (lines 1-36) - simple calculator with `main()` guard.
8. `nivel-2/nivel2.3.py` (lines 1-29) - leap-year logic with `main()` guard.
9. `nivel3/nivel3.1.py` (lines 1-24) - vowel counter.
10. `nivel3/nivel3.2.py` (lines 1-34) - palindrome checker.
11. `nivel3/nivel3.3.py` (lines 1-35) - initials formatter.
12. `nivel3/nivel3.4.py` (lines 1-34) - manual space-to-underscore replacement.

## Key Code

Current completed exercises cover levels 1-3 from `niveles.md`:

```python
# nivel-1/nivel1.py
resultado = celsius * 9/5 + 32
```
Teaches arithmetic, functions, return values, and user input conversion.

```python
# nivel-2/nivel2.3.py
def es_bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
```
Good example of clean conditional decomposition and boolean return.

```python
# nivel3/nivel3.1.py
def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador
```
Good beginner pattern: normalize input, iterate, accumulate, return.

```python
# nivel3/nivel3.4.py
def convertir_texto(texto):
    resultado = ""
    for letra in texto:
        if letra == " ":
            resultado += "_"
        else:
            resultado += letra
    return resultado
```
Teaches manual loops and string construction; later can be improved with list accumulation or `.replace()` once the exercise constraint is removed.

## Architecture

This is a learning repository, not an application backend yet.

- `niveles.md` is the curriculum. It lists exercises from Level 1 to Level 12: variables, operators, strings, conditionals, loops, lists, dictionaries, tuples/sets, functions, errors, files, and comprehensions.
- `nivel-1/`, `nivel-2/`, and `nivel3/` contain solved scripts for the first three levels.
- `notas/` contains teaching material. The current note focuses on moving from beginner scripts to import-safe, reusable Python modules using `def main()` and `if __name__ == "__main__":`.

The progression is visible: early files have top-level input/print code, while later files increasingly use function + `main()` + guard. That is the right direction for backend readiness, because backend code must separate pure logic from I/O and framework wiring.

## What Each File Teaches

- `niveles.md`: Full Python fundamentals roadmap. Current solved work reaches Level 3; remaining roadmap includes conditionals, loops, collections, functions, errors, files, and comprehensions.
- `notas/01-def-main-y-if-name-main.md`: Professional organization of executable Python scripts; avoids import side effects.
- `nivel-1/nivel1.py`: Numeric conversion, `float(input())`, function return, f-string output.
- `nivel-1/nivel1.2.py`: Importing from standard library, dates, integer input, simple arithmetic. Note: exercise asks age in 2026, but code uses current year.
- `nivel-1/nivel1.3.py`: Variable swapping. It first uses a temporary variable despite the exercise asking not to, then shows the Pythonic tuple swap.
- `nivel-2/nivel2.1.py`: Modulo operator and boolean helper function.
- `nivel-2/nivel2.2.py`: Calculator branching, function extraction, `main()` guard. Needs better invalid-operation and division-by-zero handling.
- `nivel-2/nivel2.3.py`: Leap-year rules; clean, correct conditional logic.
- `nivel3/nivel3.1.py`: String normalization with `.lower()`, loop counting, membership checks.
- `nivel3/nivel3.2.py`: Palindrome via slicing. Correct for simple lowercase words, but not normalized for accents/case/spaces.
- `nivel3/nivel3.3.py`: Splitting full names, uppercase initials, list building, joining.
- `nivel3/nivel3.4.py`: Manual character-by-character replacement with a loop.

## Learner Level / Progression

The learner is at early beginner moving toward solid beginner:

- Comfortable with variables, input conversion, arithmetic, functions, `return`, `if/elif/else`, loops, strings, f-strings, and simple imports.
- Starting to learn professional structure (`main()` and import guards).
- Has not yet reached backend-critical topics: robust validation, exceptions, data structures beyond simple lists, file I/O, modules/packages, testing, HTTP APIs, databases, async basics, or dependency management.

## Obvious Code / Style Issues Worth Teaching

- Top-level executable code remains in early files (`nivel-1/nivel1.py`, `nivel-1/nivel1.2.py`, `nivel-1/nivel1.3.py`, `nivel-2/nivel2.1.py`). Teach moving all `input()` and `print()` into `main()`.
- `nivel-1/nivel1.2.py` says age in 2026 but uses `datetime.now().year`; either pass target year `2026` into the function or update the message.
- `nivel-1/nivel1.3.py` uses a temporary variable before showing the tuple-swap solution; highlight that the requested Pythonic answer is `a, b = b, a`.
- `nivel-2/nivel2.2.py` catches all exceptions with bare `except`; teach catching specific errors and validating operations explicitly.
- `nivel-2/nivel2.2.py` returns `None` for unknown operations unless an exception happens; teach an explicit `else` branch.
- `nivel-2/nivel2.2.py` prompt omits `/` while code supports division.
- `nivel3/nivel3.2.py` palindrome checker should normalize case; optional next step: remove spaces and accents.
- Formatting is inconsistent: extra blank lines, spacing around `=`, `print (...)`, and indentation in `nivel3/nivel3.3.py`. Good moment to introduce PEP 8 and `ruff`/`black` later.
- Naming is mostly understandable Spanish; for backend work, consistent English identifiers may be useful if the target ecosystem/project uses English.

## Recommended Backend Learning Path Using This Repo

1. Finish `niveles.md` Levels 4-12 without skipping: conditionals, loops, lists, dictionaries, sets, functions, errors, files, comprehensions.
2. After each exercise, refactor into:
   - pure function(s) that receive values and return values;
   - `main()` that handles input/output;
   - `if __name__ == "__main__": main()` guard.
3. Add simple tests with `pytest` for each pure function before moving to backend frameworks.
4. Create a `src/` package and move reusable functions into modules; keep CLI scripts separate.
5. Build a small backend-ready project from existing exercises, for example:
   - contact agenda from Level 7;
   - inventory from Level 7;
   - safe calculator API.
6. Introduce FastAPI only after functions, dictionaries/lists, validation, and exceptions are comfortable.
7. Backend sequence after fundamentals:
   - Python modules/packages;
   - pytest;
   - virtual environments and `requirements.txt`/`pyproject.toml`;
   - FastAPI routes;
   - Pydantic models;
   - CRUD with in-memory dictionaries;
   - file persistence;
   - SQLite/PostgreSQL;
   - authentication basics;
   - Docker and deployment basics.

## Start Here

Open `niveles.md` first. It defines the whole curriculum and shows the learner has completed Levels 1-3 while the next natural step is Level 4 conditionals. Then open `notas/01-def-main-y-if-name-main.md` because it gives the structural rule that should be applied retroactively to the early scripts before continuing.

## Supervisor coordination

No supervisor decision was needed. Engram memory tools were not available in this subagent toolset, so no persistent memory save was performed.