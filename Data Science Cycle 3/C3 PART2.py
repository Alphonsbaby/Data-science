####      1.   Use appropriate functions in pandas to display
      
    ##• Shape of the data set
    ##• First 5 and last five rows of data set(head and tail)
    ##• Size of dataset
    ##• No:of samples available for each variety
    ##• Description of the data set( use describe


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
col=['sepal_length','sepal_width','petal_length','petal_width','type']
iris=pd.read_csv("iris.csv",names=col)
print("First five rows")
print(iris.head())
print("*********")
print("columns",iris.columns)
print("*********")
print("shape:",iris.shape)
print("*********")
print("Size:",iris.size)
print("*********")
print("no of samples available for each type") 
print(iris["type"].value_counts())
print("*********")
print(iris.describe())


##2.Use  pairplot() function to display pairwise relationships between attributes. Try different kind of plots  {‘scatter’, ‘kde’, ‘hist’, ‘reg’}  and different kind of markers

import numpy as np
import pandas as pd
import seaborn as sns 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


iris = sns.load_dataset('iris')
my_data_frame = pd.DataFrame(iris)


g = sns.pairplot(my_data_frame)
g = sns.pairplot(iris, kind="reg", hue="species")
g = sns.pairplot(iris, kind="hist", hue="species")
g = sns.pairplot(iris, kind="kde", hue="species")
g = sns.pairplot(iris, kind="scatter", hue="species")


##3.using the iris data set,get familiarize with functions:
##1)relplot()
import seaborn as sns
sns.set(style ="ticks")
  
dataset = sns.load_dataset('iris')
col=['sepal_length','sepal_width','petal_length','petal_width','type']
sns.relplot(x ="sepal_length", y ="petal_width", data = dataset)


##2) histplot()

import seaborn as sns
import pandas
import matplotlib.pyplot as plt
sns.get_dataset_names()
df = sns.load_dataset('iris')
df.head()
sns.histplot(x = 'sepal_length',kde=True,bins = 6 , data =df)

###3)displot
import seaborn as sns
import pandas
Import matplotlib.pyplot as plt
sns.get_dataset_names()
df = sns.load_dataset('iris')
df.head()
sns.displot(x = 'sepal_length',kde=True,bins = 5 , data =df)



# In[ ]:




