#Write a Python program to show a color-coded parallel coordinates plot for the wine data to give some idea of how well correlated the attributes are with the targets.
#However, your plot may suffer from compressing the graph along the variable directions that have smaller scale values.
#To overcome this limitation, you should normalize the wine data and re-plot it. 
#Compare the resulting plots between the normalized data and the raw data.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep =';')
df1=pd.DataFrame(df)
input_data= df1.loc[:,df1.columns!='quality']
target=df1['quality']

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 25
fig_size[1] = 20
plt.rcParams["figure.figsize"] = fig_size
plt.figure()

fig= pd.plotting.parallel_coordinates(
     df1[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',
                                            'free sulfur dioxide','total sulfur dioxide','density','pH','sulphates',
                                            'alcohol','quality']],'quality', 
        color= ('#556270','#4ecdc4','#c7f464','#ff6b6b','#c44d58','#ecca2e'))

plt.show()

from sklearn import preprocessing
input_data_X=preprocessing.normalize(input_data)
inputdata = pd.DataFrame(input_data_X, columns = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',
                                            'free sulfur dioxide','total sulfur dioxide','density','pH','sulphates',
                                            'alcohol'])
target=pd.DataFrame(target)

data_normalized = pd.merge(inputdata,target,how = 'left',left_index = True, right_index = True)

fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 25
fig_size[1] = 20
plt.rcParams["figure.figsize"] = fig_size
plt.figure()

fig= pd.plotting.parallel_coordinates(
     data_normalized[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides',
                                            'free sulfur dioxide','total sulfur dioxide','density','pH','sulphates',
                                            'alcohol','quality']],'quality', 
        color= ('#556270','#4ecdc4','#c7f464','#ff6b6b','#c44d58','#ecca2e'))

plt.show()
