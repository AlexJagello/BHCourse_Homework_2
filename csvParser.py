import os

class CsvParser:
     #Simple csv parser
     #
     def __init__(self, path: str):        
          self._text = ""
          self._dicts  = [] #[{:,:},{:,:}] list of dictionaries
          self._header = [] #list of headers 
          self.__read(path)
          self.__parse()


     def __read(self, path: str): 
        #just read text from file  
        f = open(path, encoding='utf-8')
        self._text = f.read()


     def __parse(self):
          #create list of dictioanries from text         
          splitedText = self._text.strip('\n').split('\n')

          for headElem in splitedText[0].split(','):
                self._header.append(headElem)

          for line in splitedText[1:]:
              subdict={}
              for item, headeritem in zip(line.split(','), self._header):
                    subdict.update({headeritem : item})
              self._dicts.append(subdict)


     def __getitem__(self, key: int):
        #you can get item of _dicts by int key
        return self._dicts[key]
     

     def __str__(self):
          string = self._header.__str__() + "\n"
          for item in self._dicts:
               string += item.__str__() + "\n"

          return string

if __name__ == "__main__":
     data = CsvParser( os.getcwd() + "\\resources\\exoplanets.csv")
     print(data)