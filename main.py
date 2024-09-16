from typing import List
from Parser import MyParser
from exoplanet import Exoplanet
from exoplanet import ExoplanetDataFrame
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pandas as pd

def showPairPlot(df:pd.DataFrame, len:int):
    sns.pairplot(df.head(len))
    plt.show()

def showHistogramm(df:pd.DataFrame, len:int, columnName:str):
    sns.histplot(df[[columnName]].head(len))
    plt.show()

def showLinear(df:pd.DataFrame, len:int, firstColumnName: str, secondColumnName: str):
    sns.lineplot(data = df.head(len),x = firstColumnName, y = secondColumnName)
    plt.show()

def fillInEmpty(exoplanetDF:ExoplanetDataFrame):
    exoplanetDF.fillInEmptyValues('median')
    print(exoplanetDF.strPercentageNullDict())

data = MyParser(os.getcwd() + "\\resources\\exoplanets.csv")
exoplanetDataFrame = ExoplanetDataFrame()
exoplanetDataFrame.fromDict(data.standardDict)
print(exoplanetDataFrame.strPercentageNullDict())
#fillInEmpty(exoplanetDataFrame)


df = pd.DataFrame(data=exoplanetDataFrame.dictOfColumns)
df1= df[['Mass', 'Radius', 'Period', 'Semi-major axis', 'Temp', 'Distance', 'Host star mass', 'Host star temp']]

showPairPlot(df1[['Mass', 'Radius', 'Period', 'Temp', 'Host star mass', 'Host star temp']],400)

#showHistogramm(df,500,'Mass')

#showLinear(df,  500, 'Mass', 'Radius')