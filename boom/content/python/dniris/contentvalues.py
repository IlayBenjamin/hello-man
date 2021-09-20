class ContentValues:

  def __init__ (self):
    self.__dictionary = {}
    
  def put (self, key, value):
    self.__dictionary.update({key : value})

  def get_values (self):
    return list(self.__dictionary.values())

  def get_keys (self):
    return list(self.__dictionary.keys())

  def get(self, key):
    return self.__dictionary.get(key)
