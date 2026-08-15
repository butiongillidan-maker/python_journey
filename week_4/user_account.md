# Day 22 — User Account Management (OOP Fundamentals)

## What does this app do?

An Object-Oriented Python script that uses a custom `UserAccount` class blueprint to manage user identities, encapsulate account state properties, and provide operational methods to display details or mutate status.

---

## Goal

* [✓] Define a custom class (`UserAccount`) with an `__init__` constructor method
* [✓] Encapsulate data attributes (`username`, `role`, and default `is_active`) within the instance context using `self`
* [✓] Implement a getter method (`get_details`) returning structured instance properties
* [✓] Implement a state mutation method (`deactivate`) modifying internal instance flags dynamically
* [✓] Instantiate class objects and verify state transitions during runtime

---

## Step By Step Logic

START Define `UserAccount` class blueprint

Implement `__init__(self, username, role)` constructor:
* Assign `self.username = username`
* Assign `self.role = role`
* Assign default active state `self.is_active = True`

Implement `get_details(self)` method:
* Return formatted string displaying `self.username`, `self.role`, and `self.is_active`

Implement `deactivate(self)` method:
* Mutate internal state `self.is_active = False`
* Print terminal notification confirming deactivation for `self.username`

Unindent to main level and instantiate object: `user_1 = UserAccount("Dan", "Engineer")`

Call `print(user_1.get_details())` -> Outputs state with `is_active = True`

Call `user_1.deactivate()` -> Flips `is_active` to `False`

Call `print(user_1.get_details())` -> Outputs state with `is_active = False` END

---

## Errors Encountered

Encountered initial syntax confusion regarding constructor parameter ordering, indentation scope for method definitions versus top-level instantiation calls, and calling methods without invoking trailing parentheses `()`. Resolved all issues by aligning indentation levels and enforcing standard method invocation syntax.
Encountered initial syntax confusion around constructor parameters (`self` ordering), missing `def` key declarations for class methods, and calling methods without invoking parentheses `()`. Resolved all issues by enforcing correct method declaration structure and using `self` inside internal scope.
---

## Things That I've Learned

Understood how OOP encapsulates both data (attributes) and behavior (methods) into reusable blueprints. Learned how `self` acts as a direct reference to the specific object instance created from a class, allowing methods to update internal state dynamically without affecting other instances.
Understood the difference between procedural functions and object methods. Learned how `self` acts as a reference to the specific object instance created from a class blueprint, allowing methods to modify internal object state independently.
