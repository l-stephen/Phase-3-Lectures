class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Welcome {self.username}")
    
    def logout(self):
        print(f"Goodbye {self.username}")

    def view_profile(self):
        print(f"Username: {self.username}")

    def change_password(self, new_password):
        self.password = new_password
        print(f"Password changed to {self.password}")

    def delete(self):
        print("Deleting post")


#we can inherit all of the properties from the User class
class Moderator(User):
    def __init__(self, username, password):
        #calls the superclass, gives access to methods and properties
        super().__init__(username, password)
        
    def delete_post(self):
        super().delete()
        print(f"{self.username} deleted a post")


class Admin(Moderator):
    def __init__(self, username, password):
        super().__init__(username, password)

    def ban_user(self, user):
        print(f"{self.username} banned {user.username}")

    def delete_user(self, user):
        print(f"{self.username} deleted {user.username}")


user_1 = User("Stephen", "password")
user_2 = User("Sam", "password123")
user_1.login()
user_1.view_profile()
user_1.change_password("newpassword")
user_1.logout()

mod_1 = Moderator("Sarah", "password45")
mod_1.login()
mod_1.view_profile()
mod_1.change_password("newpassword")
mod_1.delete_post()
mod_1.logout()

admin_1 = Admin("Alex", "passwords")
admin_1.login()
admin_1.view_profile()
admin_1.change_password("newpassword")
admin_1.delete_post()
admin_1.ban_user(user_1)
admin_1.delete_user(user_1)
admin_1.logout()






