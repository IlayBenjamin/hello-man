from dniris.database import DNIrisDatabase
import os

class DNIrisHelper:
    READ = "r"; WRITE = "a"
    __version = 1

    def __init__(self, name, factory):
        self.__name = name
        self.__path = str(r"https://github.com/IlayBenjamin/hello-man/blob/main/boom/data/dataB.txt/" + name)
        self.__create_db (self.__path, factory)

    def __create_db(self, path, factory):
        db = DNIrisDatabase.open(path, factory, DNIrisHelper.READ)
        db.close()

    def get_readable(self):
         return DNIrisDatabase.open(self.__path, None, DNIrisHelper.READ)

    def get_writable(self):
        return DNIrisDatabase.open(self.__path, None, DNIrisHelper.WRITE)


    def database_name(self):
         return (self.__name)
    
    def on_create(self, db):
         pass
    
    def on_open(self, db):
         pass
        
