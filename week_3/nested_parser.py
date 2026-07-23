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


print(api_response["server"]["name"])
