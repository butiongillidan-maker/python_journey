# Day 15: Nested Dictionaries & Architecture-Driven Data Structures

## 📌 Concept Overview
Today, I moved away from sequential lists and transitioned into **Hash Maps (Python Dictionaries)**. I learned that dictionaries provide $O(1)$ constant time complexity for data retrieval, making them essential for high-performance databases and backend system architecture.

## 🛠️ Implementation Details
I built a centralized **User Registry System** (`user_registry.py`) utilizing nested dictionaries to manage structured user profiles dynamically.

### Key Skills Mastered:
* **Nested Data Traversal:** Chaining keys (e.g., `dict[user_id][attribute]`) to target deep layers of unstructured or nested data.
* **Defensive Error Handling:** Employing the `.get()` method to handle missing lookup keys gracefully rather than letting the script crash with a `KeyError`.
* **State Mutation:** Modifying values in memory securely without affecting other sibling keys.

---

## 🔍 Code Walkthrough & Logic

```python
# Traversal: Targets only Sarah's tier out of the nested dictionary structure
print(user_database["u_103"]["tier"])

# Mutation: Upgrading Dan's account tier directly in memory
user_database["u_101"]["tier"] = "Premium"

# Defensive Check: Attempting to look up a non-existent ID safely
find = user_database.get("u_999")

if find is None:
    print("user not found in the database registry")
