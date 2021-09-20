from dniris.helper import DNIrisHelper
from user import User
from dniris.contentvalues import ContentValues
from dniris.database import DNIrisDatabase

class UserDatabase(DNIrisHelper):
  __USERNAME = "username"
  __PASSWORD = "password"
  __DATABASE_NAME = "dataA.txt"
  __TABLE_NAME = "check"
    

  def __init__(self):
    super().__init__(UserDatabase.__DATABASE_NAME, None)
    self.__database = None

  def add_record(self, user):
    db = self.get_writable()
    cv = ContentValues()
    cv.put(UserDatabase.__USERNAME, user.get_username())
    cv.put(UserDatabase.__PASSWORD, user.get_password())
    db.insert(UserDatabase.__TABLE_NAME, cv)
    db.close()
    
    
  def get_user(self, id):
    db = self.get_readable()
    cv = db.find(UserDatabase.__TABLE_NAME, id)
    username = cv.get(UserDatabase.__USERNAME)
    password = cv.get(UserDatabase.__PASSWORD)
    user = User(username, password)
    db.close()
    return user

  def suitability_check(self, username, password):
      db = self.get_readable()
      cv = ContentValues()
      cv.put(UserDatabase.__USERNAME, username)
      cv.put(UserDatabase.__PASSWORD, password)
      id_list = []
      id_list = db.query_find(UserDatabase.__TABLE_NAME, cv)
      return id_list
      #if len(id_list) < 1:
          #l = []
          #l[0] = -2
          #return False
      #if len(id_list) >= 1:
          #return True
          
