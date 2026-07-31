import json

with open("server_logs.json", "r")as f:
    datas = json.load(f)

log_num = 0

for data in datas:
    log_num += 1
    timestamp = data["timestamp"]
    status = data["status"]
    server = data["server"]
    latency = data["latency_ms"]


log_report = {
    "total logs": log_num,
    ""
}
    


print(log_num)




    


