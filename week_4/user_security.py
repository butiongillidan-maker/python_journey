class SecureUser:
    def __init__(self, username, password ):
        self.username = username
        self.__password = password

    def change_password(self, old_password, new_password):
            if old_password == self.__password:
                self.__password = new_password
                print("password updated successfully!")
            else:
                print("ERROR: YOU INPUT THE WRONG PASSWORD!")


user = SecureUser("Dan_sec", "supermegasecret123")

user.change_password("wrongpass", "newpassword123")

user.change_password("supermegasecret123", "newpassword123")
