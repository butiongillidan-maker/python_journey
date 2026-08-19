class SecureUser:
    def __init__(self, username, password ):
        self.username = username
        self.__password = password

        def change_password(self, old_password, new_password):
            old_password = self.__password
            print("password updated successfully!")
            if not isinstance(old_password, self.__password):
                print("Error: incorrect old password access denied")

   
user = SecureUser("Dan_sec", "supermegasecret123")

print(user.__password)
