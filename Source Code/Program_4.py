#4.	Write a Python program to show the heat map of the correlations between attributes and other attributes and between the attributes and the target. 
#In your heat map, hot colors correspond to the high levels (the opposite of the color scale used in the parallel coordinates plots). 
#What correlations can you find from the heat map for the wine data? 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep =';')
df1=pd.DataFrame(df)
df1

from sklearn import preprocessing
output_data=df1['quality']
input_data=df1.loc[:,df.columns!='quality']
target=df1['quality']

input_data_X=preprocessing.normalize(input_data)
input_data_scale=preprocessing.scale(input_data)
inputdata=pd.DataFrame(input_data_scale,columns=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',
                                            'free sulfur dioxide','total sulfur dioxide','density','pH','sulphates',
                                            'alcohol'])

corr = inputdata.corr()
ax = sns.heatmap(
    corr, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(50, 500, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=90,
    horizontalalignment='right'
)

plt.show()

data_normalized = pd.merge(inputdata,target,how = 'left',left_index = True, right_index = True)


corr = data_normalized.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(50, 500, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=90,
    horizontalalignment='right'
)
plt.show()
