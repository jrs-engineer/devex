# Package Sorter

This repository contains a Python implementation of the `sort(width, height, length, mass)` function for Smarter Technology's robotic factory screen.

## Rules Implemented

- A package is `bulky` when:
  - `width * height * length >= 1_000_000`, or
  - any single dimension is `>= 150`
- A package is `heavy` when:
  - `mass >= 20`

Dispatch results:

- `STANDARD`: package is neither bulky nor heavy
- `SPECIAL`: package is bulky or heavy
- `REJECTED`: package is both bulky and heavy

## Files

- `package_sorter.py`: implementation
- `test_package_sorter.py`: unit tests

## Run

```bash
python3 -m unittest -v
```

## Assumptions

- Inputs are numeric values in centimeters and kilograms.
- Negative dimensions or mass are treated as invalid input and raise `ValueError`.
