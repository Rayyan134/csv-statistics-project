# CSV Statistics Project (Beginner Python)

## Overview

This project reads a CSV file containing numbers, processes them in Python, and generates a summary CSV file with basic statistics.

It demonstrates a simple **data pipeline**:
Input --> Processing --> Output

---

## Files in this project

- `numbers.csv` --> input data file (list of numbers)
- `stats.py` --> main Python program
- `summary.csv` --> output file (generated after running script)

---

## What the program does

1. Reads numbers from `numbers.csv`
2. Converts them into a Python list
3. Calculates:
   - Mean (average)
   - Maximum value
   - Minimum value
4. Writes results into `summary.csv`

---

## How to run

Make sure you are inside the project folder, then run:

```bash
python stats.py
