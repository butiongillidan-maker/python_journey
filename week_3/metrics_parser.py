# Server cluster CPU utilization metrics
cluster_metrics = {
    "node_alpha": 42,
    "node_beta": 88,
    "node_gamma": 15,
    "node_delta": 94,
    "node_epsilon": 61
}
total_cpu = 0 
for node_name, cpu_values in cluster_metrics.items():
    if cpu_values >= 80:
        print(f"ALERT ! {node_name} ---> {cpu_values}")
    else:
        print(f"its safe your node is: {node_name} --> {cpu_values}")

    total_cpu+= cpu_values

average_cpu = total_cpu / len(cluster_metrics)
print(f"\n cluster average cpu utilization is {average_cpu}")







