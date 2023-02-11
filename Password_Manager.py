# Python Training certificate course
# Project 2 : password manager

class BasePasswordManager:
    old_password = ["parth", "Hello", "SowmyaP"]

    def get_password(self):
        # method that returns the current password as a string.
        return self.old_password[-1]

    def is_correct(self, stringg):
        # that receives a string and returns a boolean
        if stringg == self.old_password[-1]:
            print("Password Is Correct")
            return True
        else:
            print("Password Is Wrong")
            return False


# This class inherits from BasePasswordManager
class PasswordManager(BasePasswordManager):

    def __init__(self):
        self.level_old = 0
        self.level_new = 0
        BasePasswordManager.__init__(self)

    def get_level(self, string):
        self.password = string
        a, n, d = 0, 0, 0
        for i in self.password:
            if i.isalpha():
                a = a+1
            elif i.isdigit():
                n = n+1
            else:
                d = d+1
        if len(self.password) == a:
            return 0
        if len(self.password) == a+n:
            return 1
        if len(self.password) == a+n+d:
            return 2

    def set_password(self, stringg):
        Previous_password = BasePasswordManager.get_password(self)
        self.level_new = self.get_level(stringg)
        self.level_old = self.get_level(Previous_password)

        if self.level_new >= self.level_old and len(stringg):
#self.old_password.append(stringg)
            print("New password sucessfully added and securitylevel ", self.level_new)
            print("\n")
            print("New password is",stringg)
        else:
            print("Password is weak and lower security level than past password")


current = PasswordManager()

print("\n")
print("Current Password is " + current.get_password())
print("\n")
current.is_correct("SowmyaP")
print("\n")
current.set_password("Som_partha_1234")
print("\n")
