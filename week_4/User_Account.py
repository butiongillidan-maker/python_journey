class UserAccount:
    def __init__(self, username, role):
        self.username = username
        self.role = role
        self.is_active = True

    def get_details(self):
        return f"this {self.username}, and his {self.role}, - {self.is_active}"

    def deactivate(self):
        self.is_active = False
        print(f"Your account {self.username} has been deactivated.")

        user_1 = UserAccount("Dan_engineer", "Head")
        print(user_1.get_details())
        user_1.deactivate()
        print(user_1.get_details())
    

        

        

 
    
    

    
    
