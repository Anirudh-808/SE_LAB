# ISSUES FILE

**By:** Anirudh Nagarajan (PES2UG24CS065)

## Issues Identified and Fixes

| Issue | Type | Line(s) | Description | Fix approach |
|---|---|---|---|---|
| `def record_reading(meter_id, units, history=[])` | `dangerous-default-value` | 12 | Dangerous default value `[]` as argument. | Use `None` as the default value and create a new list inside the function when no history is provided. |
| `except:` | `bare-except` | 44 | No exception type(s) specified. | Replace the bare exception handler with specific exception types so that expected file and JSON errors are handled without suppressing unrelated exceptions. |
| `f = open(file)` and `f = open(file, "w")` | `unspecified-encoding` | 42, 48 | Using `open` without explicitly specifying an encoding. | Add an explicit UTF-8 encoding to file operations to avoid dependence on platform-specific default encodings and ensure consistent text processing. |
| File operations without a `with` statement | `consider-using-with` | 42, 48 | No file closing statement. | Put file operations inside a `with` statement to ensure reliable resource cleanup, prevent file handles from remaining open, and simplify the implementation. |
| `record_reading("M-01", eval(adjustment))` | `eval-used` | 63 | Use of `eval`, which is dangerous. | Replace `eval()` with `int()` to restrict user input to integer values. This prevents arbitrary Python expressions from being executed and reduces the risk of code injection. |

## EXTRA IMPROVEMENTS TO GET 10 (from 7.42) IN PYLINT

The following improvements were identified in the Pylint report. They are intended to improve code readability, maintainability, and compliance with Python conventions.

| Issue | Pylint code | Line(s) | Fix approach |
|---|---|---|---|
| Missing module docstring | `C0114` | 1 | Add a short module docstring at the beginning of the file describing the purpose of the energy system script. |
| Missing function docstrings | `C0116` | 12, 19, 28, 34, 41, 49, 53 | Add a concise docstring immediately below each function definition to explain what the function does. |
| Unnecessary `elif` after `return` | `R1705` | 21 | Replace `elif` with `if` after the preceding branch returns, and remove the unnecessary `else` where appropriate. |
| Use of global statement | `W0603` | 29, 42 | Refactor functions so that data is passed through parameters and returned from functions instead of modifying global variables. For example, have `raise_rates()` return updated rates and `load_meter_data()` return the loaded meter dictionary. |
| Old-style string formatting | `C0209` | 60, 61, 73 | Replace `%` string formatting with f-strings, preserving two decimal places with `:.2f`. |
| Unused import | `W0611` | 2 | Remove `import sys` because it is not used in the script. |
| Trailing whitespace | `C0303` | 70 | Remove spaces at the end of the affected line. |

## Verification

After applying the changes, rerun Pylint:

```bash
pylint energy_system.py
```

The expected score depends on the Pylint version and configuration used. Review the new report and address any remaining warnings rather than assuming a particular score.
