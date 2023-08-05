#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARMA
from statsmodels.tsa.ar_model import AR


# In[5]:


df = pd.read_csv("stock_data.csv", parse_dates = True, index_col="Date")
df.head()


# In[8]:


df.drop(columns = 'Unnamed: 0')


# In[9]:


df['Volume'].plot()


# In[14]:


df.plot(subplots = True, figsize=(4, 8))


# In[19]:


df_month = df.resample("Y").mean()

fig, ax = plt.subplots(figsize = (10,6))

ax.bar(df_month['2016':].index,
       df_month.loc['2016':, "Volume"],
        width = 25, align = 'center')


# In[20]:


df.Low.diff(2).plot(figsize=(6, 6))


# In[21]:


window_size = 50
rolling_mean = df['Open'].rolling\
(window_size).mean()
rolling_mean.plot()


# In[ ]:




