# Day 24 — Encapsulation & Private Attributes

## What does this app do?

An Object-Oriented Python script demonstrating data encapsulation and protection by hiding sensitive user credentials (`__password`) behind private attributes and controlling state modification via validated setter methods.

---

## Goal

* [✓] Define a `SecureUser` class encapsulating sensitive state variables
* [✓] Use double underscores (`__`) to define private attributes (`self.__password`)
* [✓] Implement a controlled setter method (`change_password`) enforcing identity verification
* [✓] Verify that unauthorized state modifications fail while valid requests succeed

---

## Step By Step Logic

START Define `SecureUser` class:
* Constructor `__init__(self, username, password)` sets public `self.username` and private `self.__password`

Implement `change_password(self, old_password, new_password)`:
* Check `if old_password == self.__password:`
  * TRUE: Update `self.__password = new_password` and print success message
  * FALSE: Execute `else:` block and print access denied error

Instantiate object: `user = SecureUser("Dan_sec", "Supermegasecret123")`

Execution sequence:
1. Call `user.change_password("wrongpass", "newpassword123")` -> Fails validation, prints ERROR
2. Call `user.change_password("supermegasecret123", "newpassword123")` -> Passes validation, updates password, prints SUCCESS END

---

## Errors Encountered

Encountered initial `AttributeError` due to indenting the `change_password` method definition inside `__init__`, causing Python to treat it as a local function rather than an instance method. Resolved by properly unindenting the method to align with class level scope.

---

## Things That I've Learned

Learned how Encapsulation protects internal object state using private attributes (`__`). Understood how setter methods act as security gates to prevent direct, unvalidated external modification of critical application data.
