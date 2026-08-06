import json

with open("raw_users.json", "r")as f:
    users = json.load(f)

    active_users = []
    security_alerts = []

    for user in users:
        if user["active"] == True and user["email_verified"] == True:
            user["status"] = "Verified"
            active_users.append(user)

                    
        if user["failed_logins"] > 10:
            security_alerts.append({"username": user["username"], "failed_logins":
            user["failed_logins"]})

            with open("sannitized.json", "w")as f:
                json.dump(active_users, f, indent = 4) 

            with open("security_audit", "w")as f:
                json.dump(security_alerts, f, indent = 4)


            print("Sanitation Commplete!")
            print(f"Active users saved: {len(active_users)}")
            print(f"Security Alerts Generated: {len(security_alerts)}")

            
             
    
