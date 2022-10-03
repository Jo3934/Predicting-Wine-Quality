#Write a Python program to find the size of the data, including the number of columns and number of rows. Your code should also explore all columns and show the data type and range for each column.
#importing csv module 
import csv 
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
#csv file name 
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep =';')


total_rows = len(df.axes[0])
total_columns = len(df.axes[1])
print("Number of Rows : "+str(total_rows))
print("Number of Columns: "+str(total_columns))
print("\nData Type of Columns:")
print (df.dtypes)
print("\n")
for num in range(0,12):
        print("Range for " + str(df.columns[num])+ " is: " +  str(df.iloc[:, num].min()) + "  " + str(df.iloc[:, num].max()))
