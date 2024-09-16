import re

class JsonParser:
     #Simple json parser
     #dont support nested objects
     def __init__(self, path: str):        
          self._text = ""
          self._dicts = []
          self.__read(path)
          self.__parse()


     def __read(self, path: str):
        #just read text from file   
        f = open(path, encoding='utf-8')
        self._text = f.read()

     def __findAllStrings(self, text, start_str, end_str):
          #find all strings between two substrings
          #text - all text, start_str - left separator, end_str - right separator
            parts = text.split(start_str)
            results = []
            for part in parts[1:]:
                remaining_text_parts = part.split(end_str, 1)
                if len(remaining_text_parts) == 2:
                    substring = remaining_text_parts[0]
                    results.append(substring)
            return results       
     

     def __parse(self):
          #create list of dictioanries from text                  
         listOfline = self.__findAllStrings(self._text, "{", "}")
         for line in listOfline:
             listOfFloatProperties = re.findall("\"([^\"]*)\":\s([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?", line)
             listOfStringProperties = re.findall( " \"([^\"]*)\":\s+\"([^\"]*)\"", line)
             listOfProperties = listOfFloatProperties + listOfStringProperties
             subdict = {}
             for property in listOfProperties:
                subdict.update({property[0]: property[1]})

             self._dicts.append(subdict)
            
       

     def __getitem__(self, key: int):
      #you can get item of _dicts by int key
        return self._dicts[key]
     

     def __str__(self):
          string = ""
          for item in self._dicts:
               string += item.__str__() + "\n"

          return string

if __name__ == "__main__":
     data = JsonParser("C:\\Users\\Alwx\\Desktop\\PythonProjects\\Homework2_ver2\\resources\\exoplanets.json")
     print(data[0])