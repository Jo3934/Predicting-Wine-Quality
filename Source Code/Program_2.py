
#Write a Python program to produce summaries of the wine data set. 
#Your code should print out a numeric summary of the data, which is included at the bottom of the code.
#Your code should also generate a box plot of the normalized variables so that you can visualize the outliers in the data. 
#Normalization means centering and scaling each column so that a unit of attribute 1 means the same thing as a unit of attribute 2.
import csv 
import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep =';')
df.describe().to_csv('summary.csv',header = True)
mms = Normalizer()
xn = mms.fit_transform(df)
df1=pd.DataFrame(xn,columns = df.columns)
df1=df1.round(2)
df1.to_csv('normalized data.csv',header = True,index = False)
boxplot = df1.boxplot()
plt.show()
