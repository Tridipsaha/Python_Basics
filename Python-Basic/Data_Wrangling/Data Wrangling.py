#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data={ 'Name': ['jai', 'Tridip', 'Akash', ' Aman'],
       'Age' : [12, 14, 13, 20,],
       'Gender': ['M', 'M', 'F', 'M'],
       'Marks': [ 76, 'NaN', 'NaN', 71] }

dataSet= pd.DataFrame(data)

dataSet


# In[3]:


c = avg = 0
for ele in dataSet['Marks']:
    if str(ele).isnumeric():
        c+=1
        avg+= ele
avg/=c
dataSet= dataSet.replace(to_replace= "NaN", value=avg)
dataSet


# In[4]:


dataSet['Gender']= dataSet['Gender'].map({'M':0, 'F':1,}).astype('int')
dataSet


# In[5]:


dataSet = dataSet[dataSet['Marks'] >= 70].copy()
dataSet


# In[6]:


details = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'NAME': ['Jagroop', 'Praveen', 'Harjot','Pooja'],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE']})

print(details)


# In[7]:


fees_status = pd.DataFrame({
    'ID': [101, 102, 103, 104],
    'PENDING': ['5000', '250', 'NIL','9000']})

print(fees_status)


# In[8]:


print(pd.merge(details,fees_status, on='ID'))


# In[9]:


car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti',
                            'Maruti', 'Hyundai', 'Hyundai',
                            'Toyota', 'Mahindra', 'Mahindra',
                            'Ford', 'Toyota', 'Ford'],
                    'Year': [2010, 2011, 2009, 2013,
                            2010, 2011, 2011, 2010,
                            2013, 2010, 2010, 2011],
                    'Sold': [6, 7, 9, 8, 3, 5,
                            2, 8, 7, 2, 4, 2]}


dataSet = pd.DataFrame(car_selling_data) 
grouped = dataSet.groupby('Year')
print(grouped.get_group(2010))


# In[10]:


non_duplicate = dataSet[~dataSet.duplicated('Year')] 
print(non_duplicate)


# In[31]:


data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]}

data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
        'Age':[22, 32, 12, 52],
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]}

dataset1= pd.DataFrame(data1,index=[0,1,2,3])
#dataset1
dataset2=pd.DataFrame(data2,index=[4,5,6,7])

res=pd.concat([dataset1,dataset2])
res


# In[ ]:





# In[ ]:




