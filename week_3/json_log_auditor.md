# Day 20 — JSON Log Auditor and Aggregation Engine

## What does this app do?

A script that simulates an automated security and performance auditing engine by parsing raw JSON server logs from disk, calculating system failure rates and latency averages across active nodes, and exporting a structured summary report to a new JSON file.

---

## Goal

* [✓] Parse real-world structured log arrays from external JSON files using `json.load()`
* [✓] Filter and flag target node failures matching condition thresholds (`status != 200` and `status == 500`)
* [✓] Compute aggregate global metrics (total log volume and average request latency) across dynamic list records
* [✓] Export structured analytical reports back to disk using `json.dump()` with clean formatting

---

Step By Step Logic

START Open `server_logs.json` with a context manager (`with open(...)`) in read mode

Load JSON payload into a list of dictionaries named `datas` using `json.load()`

Initialize tracking variables: `total_logs = 0`, `failed_requests = 0`, `flagged_servers = []`, and `total_latency = 0`
