user_database = {
    "u_101": {
        "name": "Dan",
        "role": "Student",
        "tier": "Free",
        "status": "Active"
    },
    "u_102": {
        "name": "Alex",
        "role": "Moderator",
        "tier": "Premium",
        "status": "Active"
    },
    "u_103": {
        "name": "Sarah",
        "role": "Admin",
        "tier": "Enterprise",
        "status": "Suspended"
    }
}


print(user_database["u_103"]["tier"])
user_database["u_101"]["tier"]= "Premium"


find = user_database.get("u_999")

if find is None:
    print("user not found in the database registry")

print(user_database["u_101"])
