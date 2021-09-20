from dniris.helper import DNIrisHelper
from dniris.encrypt import Encrypt
from dniris.userdb import UserDatabase
from user import User


def find_username(id):
    file = open(r'C:\Users\User-MR\Documents\GitHub\packetsecondcodeofficial.github.io\data\dataB.txt', 'r')
    line_number = (id * 4) - 3
    username = file.readlines()[line_number]
    file.close()
    return (str(username))

def find_password(id):
    file = open(r'C:\Users\User-MR\Documents\GitHub\packetsecondcodeofficial.github.io\data\dataB.txt', 'r')
    line_number = (id * 4) - 2
    password = file.readlines()[line_number]
    file.close()
    return (str(password))

def update(user):
    users_db = UserDatabase()
    users_db.add_record(user)

def delete_temp():
    file = open(r'C:\Users\User-MR\Documents\GitHub\packetsecondcodeofficial.github.io\data\dataB.txt', 'w')
    file.write(" ")
    file.close


id = -1
file = open(r'C:\Users\User-MR\Documents\GitHub\packetsecondcodeofficial.github.io\data\dataC.txt', 'r')
id = int(file.read())
file.close()
name = find_username(id)
password = find_password(id)
user = User(name, password)

update(user)

delete_temp()

#users_db.add_record(User("IlayB", "Benjamin1234"))
#users_db.add_record(User("StavMaymon", "HelloWorld2004"))

#print (users_db.get_user(1).to_string())


#print (users_db.get_user(3).get_username())
#users_db.add_record(userA)
#users_db.add_record(userB)

#print(x.database_name())

##Encrypt.print_all()


