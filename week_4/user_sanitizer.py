import json

with open("raw_user.json", "r")as f:
    json.load(f)

    active_users = []
    security_alerts = []

    for user in users:
        if user["active"] == True and user["email_verified"] == True
        user["status"] = "Verified"
        active_users.append(user)

        if user["failed_logins"] > 10:
            security_alerts.append({"username": user["username"], "failed_logins":
            user["failed_logins"]})

            
             
    
