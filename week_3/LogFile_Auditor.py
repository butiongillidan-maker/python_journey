raw_logs = [
    "INFO: System boot complete",
    "ERROR: Database connection failed",
    "WARN: Low disk space",
    "CRITICAL: Unauthorized login attempt",
    "INFO: User logged out"
]

alerts = []

for index, raw_log in enumerate(raw_logs, start=1):
    if "ERROR" in raw_log or "CRITICAL" in raw_log:
        formatted_line = f"line {index}: {raw_log} That find"
        print(formatted_line)
        
        alerts.append(formatted_line)


sorted_alerts = sorted(alerts)

print("\nSorted Alerts:")
for alert in sorted_alerts:
    print(alert)
    
