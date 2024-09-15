class CsvParser:
     def __init__(self, path: str):        
          self._text = ""
          self._dicts  = [{}]
          self._header = []
          self.__read(path)
          self.__parse()


     def __read(self, path: str): 
        f = open(path, encoding='utf-8')
        self._text = f.read()


     def __parse(self):         
          splitedText = self._text.split('\n')
          self._header = splitedText[0].split(',')
          for line in splitedText[1:]:
              subdict={}
              for item, headeritem in zip(line.split(','), self._header):
                    subdict.update({headeritem : item})
              self._dicts.append(subdict)


     def __getitem__(self, key: int):
        return self._dicts[key]
     

     def __str__(self):
          string = self._header.__str__() + "\n"
          for item in self._dicts:
               string += item.__str__() + "\n"

          return string

if __name__ == "__main__":
     data = CsvParser("C:\\Users\\Alwx\\Desktop\\PythonProjects\\Homework2_ver2\\resources\\exoplanets.csv")
     print(data)