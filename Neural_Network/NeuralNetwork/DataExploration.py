# this module contains all data exploration, analysis and visualization methods

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataExploration():
    def __init__(self, data):
        self.data = data
        
    def DisplayData(self):
        return self.data.head()
    
    def DisplayDataTypes(self):
        return self.data.dtypes
    
    def DisplayDataInfo(self):
        self.data.info()
    
    def DisplayDataDescription(self):
        return self.data.describe()
    
    def DisplayDataShape(self):
        return self.data.shape
    
    def DisplayMissingValues(self):
        return self.data.isnull().sum()
    
    def DisplayCorrelationMatrix(self):
        return self.data.corr()
    #correletion with a specific column
    def DisplayCorrelationWithColumn(self, column):
        return self.data.corrwith(self.data[column])
    
    def DisplayHeatMap(self):
        sns.heatmap(self.data.corr(), annot=True)
        plt.show()
    
    def DisplayPairPlot(self):
        sns.pairplot(self.data)
        plt.show()
    
    def DisplayCountPlot(self, column):
        sns.countplot(self.data[column])
        plt.show()
    
    def DisplayBoxPlot(self, column):
        sns.boxplot(self.data[column])
        plt.show()
       
    def DisplayScatterPlot(self, x, y):
        plt.scatter(self.data[x], self.data[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.show()
    
    def DisplayHistogram(self, column):
        plt.hist(self.data[column], bins=25)
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()
    
    def information_help(self):

        print("DisplayData()                       :Display the first few rows of the DataFrame.")  
        print("DisplayDataTypes()                  :Display the data types of each column in the DataFrame.")
        print("DisplayDataInfo()                   :Display information about the DataFrame, including number of rows, columns, and data types.")
        print("DisplayDataDescription()            :Display descriptive statistics for each column of the DataFrame.")
        print("DisplayCorrelationMatrix()          :Display the correlation matrix between all numeric columns of the DataFrame.")
        print("DisplayCorrelationWithColumn(column):correletion with a specific column")
        print("DisplayHeatMap()                    :Displays a heatmap of the correlation matrix.")
        print("DisplayPairPlot()                   :This method creates a pairplot, also known as a scatterplot matrix, which shows pairwise relationships between numerical columns ")
        print("DisplayCountPlot()                  :This method generates a countplot, which is a type of bar plot that shows the frequency of each category in a categorical column of the DataFrame")
        print("DisplayBoxPlot()                    :This method creates a boxplot for a numerical column in the DataFrame.")
        print("DisplayScatterPlot()                :This method generates a scatter plot between two numerical columns in the DataFrame")
        print("DisplayHistogram()                  :This method creates a histogram for a numerical column in the DataFrame")
       

