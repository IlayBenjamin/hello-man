import re

class User:

    def __init__(self, username, password):
        self.__id = -2
        self.__username = username
        self.__password = password

    def to_string(self):
        return ("[username  = " + "'" + self.get_username() + "', password = " + "'" + self.get_password() + "'" + "]")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def is_username_standard(username):
        if type(username) == type(str()):
            if (len(username)) >= 2:
                if username.isalpha():
                    return True
        return False
    
    def is_password_standard(password):
        if type(password) == type(str()):
            if (len(password)) >= 4:
                if re.match("^[A-Za-z0-9_-]*$", password):
                    return True
        return False
