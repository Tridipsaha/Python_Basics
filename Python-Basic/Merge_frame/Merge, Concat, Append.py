#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
list = [1,2,3,4,5,6,7,8,9,10]
type(list)


# In[6]:


array1 = np.array(list)
array1


# In[9]:


newarray = array1.reshape((5,2))
newarray


# In[5]:


data={ 'Name': ['jai', 'Tridip', 'Akash', ' Aman'],
       'Age' : [12, 14, 13, 20,],
       'Gender': ['M', 'M', 'F', 'M'],
       'Marks': [ 76, 'NaN', 'NaN', 71] }

dataset = pd.DataFrame(data)
dataset


# In[18]:


dataset.pivot(index=None, columns = 'Gender', values=['Name'])


# In[20]:


details = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'NAME': ['Jagroop', 'Praveen', 'Harjot','Pooja'],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE']})

fees_status = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'PENDING': ['5000', '250', 'NIL','9000']})


print(pd.merge(details, fees_status, on='ID'))## Merging


# In[21]:


data1 = pd.DataFrame({'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]})

data2 = pd.DataFrame({'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
        'Age':[22, 32, 12, 52],
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]})

res = pd.concat([data1,data2])
res


# In[22]:


data1 = pd.DataFrame({'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]})

data2 = pd.DataFrame({'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
        'Age':[22, 32, 12, 52],
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]})

print(data1.append(data2))


# In[7]:


df = pd.DataFrame({"A":[12, 4, 5, None, 1],
"B":[7, 2, 54, 3, None],
"C":[20, 16, 11, 3, 8],
"D":[14, 3, None, 2, 6]})
df
df.transform(lambda x : x + 10)


# In[ ]:





# In[39]:


import re
txt = "in The in rain in Spain"
#Check if the string starts with "The":
x = re.findall("\Ain", txt)
print(x)


# In[ ]:




