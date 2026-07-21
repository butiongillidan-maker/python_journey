# Day 17 - Dictionary Comprehension & Data Filtering

## What does this app do?

A data cleaning utility for MLOps Pipelines that takes a raw, corrupted  dictionary of sensor reading and uses dictionary comprehension to filter out missing (-999.0) and dead (0.0) sensor metrics.

---

## Goal

* [✓] refactor multi- line dictionary filtering into a single dictionary comprehension
* [✓] filter Dynamic dataset key value pairs based on custom numeric thresholds ('>0.0)

---

## Step By Step Logic

START
Define raw_sensor_data with corrupted and valid floats

Use dictionary comprehension to construct cleaned_data:
Map key:value pairs (sensor:data)
Iterate over raw_sensor_data.items()
Apply condition: Keep only if data > 0.0

Print cleaned_data
END

---

## Errors Encountered

None during execution. Tested the condition logic using standard iteration before compressing into a one-line dictionary comprehension syntax.

---

## Things That I've Learned

How to condense multi-line loop/conditional logic into single-line dictionary comprehensions '{k: v for v in dict.items() if condition}. How dataset cleaning operates in backend pipelines before passing pay loads to analitical mode.  

