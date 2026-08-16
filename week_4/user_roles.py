class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def get_info(self):
        return f"User : {self.username} - {self.email}"
    
class Admin(User):
    def Delete_user(self, target_user):
        print(f"Admin {self.username} deleted user {target_user}.")

standard_user = User("Boss DanDan", "Dan@admin.com")
admin_user = Admin("illidan", "illidan@stormrage.com")
print(admin_user.get_info())
print(standard_user.get_info())
admin_user.Delete_user("Boss DanDan")
   
       


        
