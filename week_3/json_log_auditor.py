import json


with open("server_logs.json", "r") as f:
    datas = json.load(f)


total_logs = 0
failed_requests = 0
flagged_servers = []
total_latency = 0


for data in datas:
    total_logs += 1
    total_latency += data["latency_ms"]
    
  
    if data["status"] != 200:
        failed_requests += 1
        
    
    if data["status"] == 500:
        flagged_servers.append(data["server"])


avg_latency = total_latency / total_logs


report = {
    "total_logs_processed": total_logs,
    "failed_count": failed_requests,
    "flagged_servers": flagged_servers,
    "average_latency_ms": avg_latency
}


with open("audit_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("Audit report generated successfully!")
