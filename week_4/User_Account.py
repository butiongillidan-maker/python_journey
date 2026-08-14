class UserAccount:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.is_active = True

    def get_details(self):
        return f"this {self.username}, and his {self.role}, - {self.is_active}"

    def deactivate(self):
        set.is_active = False
        print(f"Your account {self.username} has been deactivated.")
