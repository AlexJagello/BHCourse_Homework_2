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
    exoplanetDF.fillInEmptyValues('median') #fill empty values 
    print(exoplanetDF.strPercentageNullDict())

data = MyParser(os.getcwd() + "\\resources\\exoplanets.csv") #Parse csv or json file. we get list of dictionaries such [{:,:},{:,:}] 
exoplanetDataFrame = ExoplanetDataFrame() #create special DataFrame for exoplanet dataset
exoplanetDataFrame.fromDict(data.standardDict) # fill DataFrame from dictionary
print(exoplanetDataFrame.strPercentageNullDict()) # get percent of none value for each column
#fillInEmpty(exoplanetDataFrame) #fill None values


df = pd.DataFrame(data=exoplanetDataFrame.dictOfColumns) # create pandas DataFrame from exoplanet DataFrame. 
#ToDo try to show charts without pandas DataFrame

df1= df[['Mass', 'Radius', 'Period', 'Semi-major axis', 'Temp', 'Distance', 'Host star mass', 'Host star temp']] #select only numerical data columns

showPairPlot(df1[['Mass', 'Radius', 'Period', 'Temp', 'Host star mass', 'Host star temp']],400) #Show pair plots

#showHistogramm(df,500,'Mass') #Show Histogram for mass parameter

#showLinear(df,  500, 'Mass', 'Radius') #Show Linear dependency for Mass and Radius
