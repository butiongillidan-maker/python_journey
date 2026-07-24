api_response = {
    "status": 200,
    "server": {
        "name": "Production-Cluster-A",
        "environment": "production",
        "config": {
            "max_connections": 5000,
            "ssl_enabled": True,
            "timeout_seconds": 30
        }
    }
}


server_name = (api_response.get("server", {}).get("name", "unknown name"))
is_ssl = (api_response.get("server", {}).get("config", {}).get("ssl_enabled"))
if is_ssl:
    print(f"SUCCESS: {server_name} has SSL enabled.")
else:
    print(f" Warning: {server_name} does not have SSL Enabled.")
