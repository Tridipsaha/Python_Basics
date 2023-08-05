#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

pokemons={
    "Hight": np.random.randint(20,70,(5)),
    "Weight": np.random.randint(60,120,(5)),
    "Power": np.random.randint(120,500,(5))
}
pokemons


# In[12]:


df= pd.DataFrame(pokemons,index=[1,2,3,4,5])#Creating a frame of the data
df.head()
df.columns# showing the columns name or tuples only 


# In[7]:


df.to_csv("Pokemon_Data.csv")# create a csv file in file mannager


# In[8]:


df= pd.read_csv('Pokemon_Data.csv')# read the csv file 
df.head()


# In[17]:


#df.drop(columns=[name of that columns])# when delete any column
#df.columns=['e','r']???? adding column 


# In[27]:


arr= [3,7,8,1,0,3]
series=pd.Series(arr)
print("Series=",series)#IN a row wise print
print()
arr=series.values
print("Array= ",arr)#Print the value in coloum wise
print()
reshape=arr.reshape((3,2))
print("Reshape=",reshape)

print()
df = pd.DataFrame({'A': ['John', 'Boby', 'Mina'],
'B': ['Masters', 'Graduate', 'Graduate'],
'C': [27, 23, 21]})
df

df.pivot(index ='A', columns ='B', values =['C', 'A'])

