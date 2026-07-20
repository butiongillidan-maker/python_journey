# Day 16 — Dictionaries and Iterations and the Metrics Engine

## What does this app do?

A script that simulates an infrastructure monitoring engine by processing server cluster utilization logs, scanning for performance threshold exceptions, and dynamically aggregating collective data totals.

---

## Goal

* [✓] Iterate through key-value pairs simultaneously using `.items()`
* [✓] Isolate and flag nodes matching specific overload conditions
* [✓] Track global system states across individual data collections

---

## Step By Step Logic
START
Create a dictionary called cluster_metrics with node loads
Initialize total_cpu counter to 0

Loop through cluster_metrics extracting (node_name, cpu_values):
IF cpu_values >= 80:
Print ALERT status with node name and metric
ELSE:
Print SAFE status with node name and metric
Add cpu_values to total_cpu
Calculate average_cpu by dividing total_cpu by length of cluster_metrics
Print global average_cpu percentage
END
