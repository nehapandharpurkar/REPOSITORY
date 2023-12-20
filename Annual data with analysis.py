#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('annual_data.csv')


# In[3]:


df


# In[4]:


x=df['Period']
y=df['Asset_liability_code']
plt.bar(x,y)


# In[7]:


a=df[(df['Asset_liability_code']=='L000000')]


# In[8]:


a


# In[9]:


x=df['Period']
y=df['Inst_sector']
plt.bar(x,y)


# In[10]:


b=df[(df['Asset_liability_code']=='L000000') & (df['Inst_sector']=='Total all sectors')]


# In[11]:


b


# In[ ]:




