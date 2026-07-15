# Day 14 — Log File Auditor

## What does this app do?

A lightweight security auditing tool designed to scan raw, unsorted system log streams. It filters out non-critical clutter (like warnings and info logs), tracks the exact line position where security events occurred, and outputs a clean list of high-priority alerts sorted alphabetically for easy admin review.

---

## Goal

* [x] Use `enumerate()` to track log line indexes dynamically starting from 1.
* [x] Filter raw log data to capture only "ERROR" or "CRITICAL" entries.
* [x] Format and store processed alerts inside a dynamically populated list.
* [x] Sort the final alerts list alphabetically while leaving the original logs untouched.

---

## Step By Step Logic

```text
START
Create a list of raw log strings (raw_logs)
Create an empty list called alerts

Loop through raw_logs with index tracking (starting at index 1):
    IF "ERROR" is in raw_log OR "CRITICAL" is in raw_log:
        Format string: "line {index}: {raw_log} That find"
        Append formatted string to alerts list

Sort the alerts list using sorted() and assign it to sorted_alerts

Loop through sorted_alerts:
    Print each alert
END


Errors Encountered:

Initially tried checking string values using if raw_logs is "error", which compares physical memory addresses rather than string values. Fixed by shifting to the in membership operator.
Tried using if raw_log is "error" or critical which evaluated the second half of the statement as its own independent truthiness check. Fixed by making both sides of the or explicit: if "ERROR" in raw_log or "CRITICAL" in raw_log.
Tried utilizing raw_logs.sorted(), which threw an attribute error because lists do not possess a .sorted() method. Corrected to the functional sorted(alerts) approach.
Placed a premature break statement inside the final printing loop, which caused the code to execute successfully but exit instantly after displaying only the first sorted line. Fixed by removing the break so the loop could finish printing all stored alerts.


Things That I've Learned:
How enumerate(sequence, start=1) handles index increments automatically and memory-efficiently under the hood, saving us from writing manual counter variables.
The major architectural difference between list.sort() (destructive in-place sorting) and sorted(list) (generates a sorted copy). Using sorted() is crucial when we want to preserve historical or chronological source data elsewhere in the program.
How break behaves within loops and how to isolate printing loops from loop-termination mechanics.
