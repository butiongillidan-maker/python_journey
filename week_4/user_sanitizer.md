# Day 21 — User Security & Data Sanitizer Pipeline

## What does this app do?

A data pipeline script that ingests raw user database records from a JSON file, filters out inactive or unverified accounts, flags security risks based on excessive failed login attempts, and exports sanitized user datasets and security audit reports to separate JSON files.

---

## Goal

* [✓] Load and parse multi-record JSON database exports using `json.load()`
* [✓] Apply compound conditional filtering (`active == True` and `email_verified == True`) to isolate valid records
* [✓] Dynamically inject new schema keys (`"status": "VERIFIED"`) into validated dictionaries
* [✓] Detect security anomaly thresholds (`failed_logins > 10`) and isolate alert payloads
* [✓] Export multiple categorized output files using `json.dump()` with `indent=4` formatting

---

## Step By Step Logic

START Open `raw_users.json` using a context manager (`with open(...)`) in read mode

Load JSON array into `users` list using `json.load()`

Initialize output containers: `active_users = []` and `security_alerts = []`

Loop through each `user` dictionary in `users`:
* IF `user["active"] == True` AND `user["email_verified"] == True`:
  * Add `"status": "VERIFIED"` key-value pair to `user`
  * Append updated `user` object to `active_users` list
* IF `user["failed_logins"] > 10`:
  * Extract `username` and `failed_logins` fields into a new dictionary
  * Append alert dictionary to `security_alerts` list

Open `sannitized.json` in write mode (`"w"`) and export `active_users` using `json.dump(..., indent=4)`

Open `security_audit` in write mode (`"w"`) and export `security_alerts` using `json.dump(..., indent=4)`

Print execution summary including `len(active_users)` and `len(security_alerts)` END

---

## Errors Encountered

Triggered a `SyntaxError: expected ':'` on line 10 due to a missing colon at the end of the compound `if` statement. Also encountered a `FileNotFoundError` caused by a typo in the input file path (`raw_user.json` instead of `raw_users.json`). Resolved both by appending the required `:` syntax and matching the exact string name of the source JSON file.

---

## Things That I've Learned

How to build an end-to-end data processing pipeline that reads raw input files, applies multi-branch validation and anomaly detection logic simultaneously, and outputs partitioned reports to disk. Reinforced proper exception handling for file paths and syntax structure.
