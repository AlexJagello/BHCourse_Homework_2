from ast import List
import inspect
from turtle import update
from typing import Dict

class ExoplanetDataFrame:
    #Data frame class. created for exoplanet dataset
    def __init__(self):
        self.dictOfColumns = {} #{"name": [data]}
        self.percentageNullDict = {} #{"name": null values in percent}

    
    def percentageOfNullValues(self) -> Dict[str,float]:
        #counts none values ​​as a percentage
        for k, v in self.dictOfColumns.items():
            nullPercent = sum(x is None or x=="" or x==" " for x in v) / v.__len__()
            self.percentageNullDict.update({k : nullPercent})    
        return self.percentageNullDict        

    
    def fromDict(self, listOfDictionaryData):        
        #transform list of dicts to dataFrame
        for k in listOfDictionaryData[0].keys():
            self.dictOfColumns.update({k:[]})

        for dict in listOfDictionaryData:        
            for k,v in dict.items():
               val = v
               #ToDo change this string. Now it is one place which related to current data set 
               if (k != 'Name' and k != 'Discovery method' and k != 'Remarks') and isinstance(v,str): 
                    val = None
               self.dictOfColumns.get(k).append(val)
        
   
    def strPercentageNullDict(self):
        #prints a string representation of the percentage empty values ​​for each column
        self.percentageOfNullValues()
        string = ""
        for k,v in self.percentageNullDict.items():
            string += k.__str__() + " : " + round((v*100)).__str__() + '% empty data\n'
        return string

    
    def fillInEmptyValues(self, mode:str):
          #fill none values by mode: median or average
          newDict = {} #{"name": [data float]}
          for k,v in self.dictOfColumns.items():
              if isinstance(v[3],str) == False:
                  newlist = self.__fillOneArray(v, mode)
                  newDict.update({k:newlist})
              else: newDict.update({k:v})
          self.dictOfColumns = newDict
                  
 
                            
                
    def __fillOneArray(self, list, mode:str):

        newlist = [x for x in list if x is not None]

        for i in range(0, len(list)):
            if isinstance(list[i], str): print(list[i] + "  "+ i.__str__())

        emptyElementValue = 0
        if mode == "average":
            emptyElementValue = sum(newlist) / len(newlist)
        if mode == "median":
            emptyElementValue = self.__median(newlist)

        list = [emptyElementValue if x is None else x for x in list]
        return list


    def __median(self, list) -> float:
        if not list:
            return None 
        sortedList = sorted(list)
        midx = (sortedList.__len__() - 1) // 2

        if sortedList.__len__() % 2 == 0: 
            return (sortedList[midx] + sortedList[midx + 1]) / 2.0
        else:  
            return sortedList[midx]


#dont use
class Exoplanet:
    def __init__(self):
        self.name = None
        self.mass = None
        self.radius = None
        self.period = None
        self.semiMajorAxis = None
        self.temp = None
        self.distance = None
        self.hostStarMass = None
        self.hostStarTemp = None
        self.discoveryMethod = None




    def fromDict(self, dictionaryData):
        if isinstance(dictionaryData, dict):
            self.name = dictionaryData.get('Name')
            self.mass = dictionaryData.get('Mass')
            self.radius = dictionaryData.get('Radius')
            self.period = dictionaryData.get('Period')
            self.semiMajorAxis = dictionaryData.get('Semi-major axis')
            self.temp = dictionaryData.get('Temp')
            self.distance = dictionaryData.get('Distance')
            self.hostStarMass = dictionaryData.get('Host star mass')
            self.hostStarTemp = dictionaryData.get('Host star temp')
            self.discoveryMethod = dictionaryData.get('Discovery method')
        else: raise Exception("variable dict not a dictionary")

    def __str__(self) -> str:
        string = ""
        for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]): 
                    string +=i.__str__() + '\n'
        return string


    def fromValues(self, name, mass, radius, period, semiMajorAxis, temp, distance, hostStarMass, hostStarTemp):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.period = period
        self.semiMajorAxis = semiMajorAxis
        self.temp = temp
        self.distance = distance
        self.hostStarMass = hostStarMass
        self.hostStarTemp = hostStarTemp


