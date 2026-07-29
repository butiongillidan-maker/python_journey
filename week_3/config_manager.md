# Day 19 — JSON File I/O and Configuration State Management

## What does this app do?

A script that reads application settings from an external JSON file into Python memory, safely updates configuration states, and exports the updated payload back into a new formatted JSON file on disk.

---

## Goal

* [✓] Read and parse external JSON datasets using `json.load()`
* [✓] Modify nested dictionary values dynamically in memory
* [✓] Write formatted JSON data back to disk using `json.dump()` with proper indentation

---

## Step By Step Logic

START Open `settings.json` using `pathlib.Path` and a context manager (`with open(...)`)

Load JSON data into a Python dictionary named `data` using `json.load()`

Modify `debug_mode` value to `True` and add a new key `environment` set to `"staging"`

Create output path object `updated_settings.json`

Open file in write mode (`"w"`) and serialize dictionary into JSON using `json.dump(data, f, indent=4)`

Print success message to console END

---

## Errors Encountered

Triggered a `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` exception because `settings.json` was initially saved as an empty file. Python tried to parse character 0 of an empty file before reaching the execution line. Fixed by populating `settings.json` with valid JSON structural data before invoking `json.load()`.

---

## Things That I've Learned

How to use `json.load()` to parse raw disk data into native Python dictionaries, and `json.dump()` to serialize RAM data back into `.json` files. Learned that Python handles data type translation automatically (e.g., Python `True` $\rightarrow$ JSON `true`). Mastered using `indent=4` to generate clean, human-readable JSON files rather than compressed single-line strings.
