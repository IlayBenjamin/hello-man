from dniris.contentvalues import ContentValues

class Encrypt:
  #Symbols
  __DICTIONARY_A = {
    "<" : "$",
    ">" : "&",
    "[int]=" : "a",
    "[str]=" : "z",
    "[float]=" : "b",
    "[double]=" : "y",
    "[blob]=" : "c",
    'open"' : "+",
    'close"' : "~"
  }

    #Symbols
  __DICTIONARY_B = {
    "Start Open Tag" : "<Record",
    "End Open Tag" : ">",
    "Close Tag" : "</Record>",
    "End Close-Open Tag" : "/>", 
    "Before Key" : "#",
    "Start Set Value" : '="',
    "End Set Value" : '"',
    "Letter Buffer" : "-",
    "Space" : " "
  }
  
  __memory = 292

  def print_all():
    print(Encrypt.__DICTIONARY_A)
    
  
  def data_query(cv, content):
        lines = content  #List of every record in table as coded lines (line = coded record = list cell).
        cv2 = ContentValues()    #cv2 is a storage of attributes and its values, like cv, # but without empty fields. #cv is a storage of attributes and its values,  # we looking for every record which match these attributes.
        keys = cv.get_keys()     #List of every attribute name.
        coded_attributes = []    #List of every attribute name + attribute value as coded data.
        index = 0                #Index of the list - coded_attributes.

        for key in keys:         #For every key in keys:
            if key != None:      #Keep Going - if key is not None:
                if cv.get(key) != None:  #Keep Going - if value of key is not None:
                    cv2.put(key, cv.get(key))    #Add attribute name (as key) with attribute value (as value) - to cv2.
                    coded_attributes.append(Encrypt.__DICTIONARY_B.get("Before Key") + key)                           #Code line = #key
                    coded_attributes[index] = (coded_attributes[index] + Encrypt.__DICTIONARY_B.get("Start Set Value"))    #Code line = #key="
                    coded_attributes[index] = (coded_attributes[index] + Encrypt.single_write(cv.get(key)))                #Code line = #key="coded_value
                    coded_attributes[index] = (coded_attributes[index] + Encrypt.__DICTIONARY_B.get("End Set Value"))      #Code line = #key="coded_value"
                    index = index + 1

        #print("coded_attributes: \n", str(coded_attributes))
        id_list = []     #List of every line id of a record which suit to the attributes.
        suit = True      #Index of the suitability of record attributes in table to the list attributes.
        index = 0        #Index of the list - id_list.
        line_counter = 0  #Counter of lines.
        keys = cv2.get_keys()

        for line in lines:   #For every line in lines (every record in table):
            for coded_attribute in coded_attributes :   #For every coded attributes in coded_attributes list, If suit is True:
                if suit:
                    if line.find(coded_attribute) == -1:             #If the coded attribute doesn't exists in the coded line, record is not suit:                                     
                        suit = False                                 #Suit = False.
            if suit == True:   #Keep Going, If suit is True:
                id_list.append(line_counter)    #Add the line_id (line_counter) to the list - id_list.
                index = index + 1                #Add 1 to line_id index.
            line_counter = line_counter + 1      #Add 1 to line_counter.
            suit = True                          #Set suit as True.
        return id_list                           #Return the id_list.


  def write(content_values):
    keys = content_values.get_keys()
    values = content_values.get_values()
    code = ""
    value = ""
    key = ""
    code = '\n' + Encrypt.__DICTIONARY_B.get("Start Open Tag")
    for index in range(0, len(keys)):
      key = Encrypt.__DICTIONARY_B.get("Before Key") + keys[index]
      value = Encrypt.__DICTIONARY_B.get("Start Set Value")
      code = code + Encrypt.__DICTIONARY_B.get("Space") + key
      digit_group = ""
      for letter in values[index]:
        digit_group = str(ord(str(letter)))
        value = value + digit_group + Encrypt.__DICTIONARY_B.get("Letter Buffer")
      value = value[:-1] + Encrypt.__DICTIONARY_B.get("End Set Value")
      code = code + value
    code = code + Encrypt.__DICTIONARY_B.get("Space") + Encrypt.__DICTIONARY_B.get("End Close-Open Tag")
    return code 

  
  def read(line_id, content):
    cv = ContentValues()
    line = content
    sub_line = line
    index_key = 0
    index_val = 0
    x = line.count("#")
    for index in range(0, x):
      #print ("index in range(0, x) --> index = " + str(index))
      start = sub_line.find('#', index_key) + 1
      #print ("start where # + 1 in sub_line after ik --> start = " + str(start) + ", ik = " + str(index_key))
      end = sub_line.find('=', start)
      #print ("end where " + '"' + " in sub_line after start --> end = " + str(end) + ", start = "+ str(start))
      key = sub_line[start : end]
      #print ("key between start:end --> key = " + key + ", start " + str(start) + ", end = "+ str(end))
      start = sub_line.find('"', index_val) + 1
      #print ("start where  " + '"' + " + 1 in sub_line after iv --> start = " + str(start) + ", iv = " + str(index_val))      
      end = sub_line.find('"', start)
      #print ("end where  " + '"' + " + 1 in sub_line after start --> end = " + str(end) + ", start = " + str(start)) 
      value = sub_line[start : end]
      #print("value --> value = " + value)
      real_value = ""
      #print("rv --> rv = " + real_value)      
      lst = value.split('-') 
      #print ("lst --> " + str(lst))
      for c in lst:
        #print("c in lst --> " + str(c))
        real_value = real_value + str(chr(int(c)))
        #print("rv --> rv = " + real_value)
      cv.put(key, real_value)
      #print("cv puts {key, rv} --> key = " + key + ", rv = " + real_value)
      index_key = end; index_val = end + 1
      lst = None
      real_value = None
      value = None; key = None
    return cv



   

  #def data_by_query(cv, content):
    #lines = content
    #line = ""
    #sub_line = ""
    #keys = cv.get_keys()
    #values = cv.get_values()
    #cv2 = ContentValues()
    #rows_id_list = []
    #for key in keys:
        #if key != None:
            #if cv.get(key) != None:
                #cv2.put(key, cv.get(key))
    
    #attributes = []
    #index = 0
    #for attribute in cv2.get_keys():
        #attributes[index] = Encrypt.__DICTIONARY_B.get("Before Key") + attribute
        #attributes[index] = attributes[index] + Encrypt.__DICTIONARY_B.get("Start Set Value")
        #attributes[index] = attributes[index] + Encrypt.single_write(cv2.get(attribute)) + Encrypt.__DICTIONARY_B.get("End Set Value")
        #index = index + 1

    #b = True
    #row = 1
    #index = 0
    #for line in lines:
        #for coded_attribute in attributes and b:
            #if line.find(codedcoded_attribute) == -1:
                #b = False
        #if b == True:
            #rows_id_list[index] = row
            #index = index + 1
        #row = row + 1
        #b = True
    #return rows_id_list
      

  def single_write(value):
    digit_group = ""
    index = 0
    x = ""
    for letter in value:
        digit_group = str(ord(str(letter)))
        x = x + digit_group + "-"
    x = x[:-1]
    return x


  def single_read(coded_value):
    lst = coded_value.split('-')
    decoded_value = ""
    for c in lst:
        decoded_value = decoded_value + str(chr(int(c))) 
    return decoded_value



