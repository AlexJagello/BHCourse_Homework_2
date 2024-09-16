from typing import List
from Parser import MyParser
from exoplanet import Exoplanet
from exoplanet import ExoplanetDataFrame
import os

def dataToExoplanetObject(data)->List[Exoplanet]:
    exoplanetList = []
    for item in data:
        expl = Exoplanet()
        expl.fromDict(item)
        exoplanetList.append(expl)




data = MyParser(os.getcwd() + "\\resources\\exoplanets.json")
exoplanetDataFrame = ExoplanetDataFrame()
exoplanetDataFrame.fromDict(data)
print(exoplanetDataFrame.strPercentageNullDict())
exoplanetDataFrame.fillInEmptyValues('average')
print(exoplanetDataFrame.strPercentageNullDict())

exoplanets = dataToExoplanetObject(data)





