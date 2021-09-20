import os
from dniris.contentvalues import ContentValues
from dniris.encrypt import Encrypt

class DNIrisDatabase:
  
  CREATE_IF_NEEDED = "CREATE TABLE IF NOT EXISTS"
  READABLE_ONLY = 1
  WRITE_AND_READ = 0

  def __init__(self):
    self.__path = None
    self.__is_open = False
    self.__flags = None
    self.__version = 1
    self.__file = None
  
  def insert (self, table, content_values):
    if self.__is_open == True:
      if True:
        new_line = Encrypt.write(content_values)
        #self.__file.close()
        self.open_db('a')
        self.__file.write(new_line)      

  def find(self, table, row_id):
    if self.__is_open == True:
      if True:
        self.open_db('r')
        row = self.__file.readlines()[row_id]
        cv = Encrypt.read(row_id, row)
        return cv
  

  def query_find(self, table, cv):
    if self.__is_open == True:
      if True:
        self.open_db('r')
        t = self.__file.read()
        content = t.split("\n")
        #print(str(content))
        id_list = Encrypt.data_query(cv, content)
        return id_list



  def create(path):
     file_new = open(path, 'x')
     file_new.close()

  def open_db(self, flags):
    if(self.__is_open == False):
      self.__file = open(self.__path, flags)
      self.__flags = flags
      self.__is_open = True

  @staticmethod
  def open(path, factory, flags):
      #Create Empty DNIrisDatabase Object (db)
      db = DNIrisDatabase()
      if db.__is_open == False: 
        #Sets db variables
        db.__path = path 
        db.__flags = flags
        db.__is_open = True
        db.__file = open(path, flags)
      else:
        print("Error database already opened!")
      return db

  def close(self):
      self.__is_open = False
      self.__file.close()
      self.__flags = None

  #Getter Functions
  def get_path(self):
    return self.__path
  
  def get_version(self):
    return self.__version
      
  def is_readable_only(self):
    return self.__flags
    
  def is_open(self):
  	return self.__is_open()

  def __len__(self):
    if self.__is_open == True:
        if True:
            lines = self.__file.readlines()
            l = len(lines)
            return l
