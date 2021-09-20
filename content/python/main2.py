from dniris.helper import DNIrisHelper
from dniris.encrypt import Encrypt
from dniris.userdb import UserDatabase
from user import User

def single_read(coded_value):
    lst = coded_value.split('-')
    decoded_value = ""
    for c in lst:
        decoded_value = decoded_value + str(chr(int(c))) 
    return decoded_value


users = UserDatabase()
name = "IlayB"
password = "Benjamin2003"
id_list = users.suitability_check(name, password)
print("Username:", name)
print("Password:", password)
print("Is suit? ---->", str(id_list))



#code = "73-108-97-121-66"
#value1 = single_read(code)
#print("Now:", value1)
#print("Old:", "IlayB")
#print ("Old == Now --->", (bool(value1 == "IlayB")))
