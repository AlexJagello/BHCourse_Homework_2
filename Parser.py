from csvParser import CsvParser
from jsonParser import JsonParser
import os
import re

class MyParser:
    #Common parser. 
    #Get from concrete parser list of dicts 
    #and transform keys and values in a convenient form
    def __init__(self, path:str):
        self._path = path
        self.standardDict = []

        if path.find("json") != -1:
             self._parser = JsonParser(path)
        elif path.find("csv") != -1:
             self._parser = CsvParser(path)
        
        self.__transformationParsedDict()

    def __getitem__(self, key: int):
        return self.standardDict[key]

    def __str__(self) -> str:
        string = ""
        for item in self.standardDict:
            string += "\n"
            for k,v in item.items():
                string +="{ "+k.__str__() + " : " + v.__str__() + " }"
        return string


    def __transformationParsedDict(self):
        for item in self._parser:
            newdict = {}
            for k,v in item.items():
                newdict.update({self.__transformKey(k):self.__transformValue(v)})
            self.standardDict.append(newdict)

    def __transformKey(self, key:str):
        openbreacketIndex = key.find('(')
        if openbreacketIndex != -1:
            propertyName = key[:openbreacketIndex]
        else: propertyName = key
        return propertyName.strip(' ').strip('.')


    def __transformValue(self, text: str) -> float:  
        textval = 0
    
        if re.search('[a-df-zA-DF-Z]', text) != None:  
            return text
        
        try:
            if isinstance(text, str):
                textval = self.__formateStringWithFloatValue(text).strip(' \'\"~<>').strip(' ')
                if textval == '': 
                    return None
                val = float(textval)
                return val
            else: return float(text)
        except: return None
       
        

    def __formateStringWithFloatValue(self, text) -> str:   
        plusminusIndex = text.find('±')
        if plusminusIndex != -1:
            return text[:plusminusIndex]       

        plusIndex = text.find('+')
        if plusIndex != -1:
             return text[:plusIndex]       

        minusIndex = text.find('−')
        if minusIndex != -1:
             return text[:minusIndex]    

        minusIndex = text.find('/')
        if minusIndex != -1:
             return text[:minusIndex]
        minusIndex = text.find('[')
        if minusIndex != -1:
             return text[:minusIndex]    
        minusIndex = text.find('-')
        if minusIndex != -1:
             return text[:minusIndex]        
        return text


if __name__ == "__main__":
     data = MyParser( os.getcwd() + "\\resources\\exoplanets.csv")
