#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("mm.csv")


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.size


# In[6]:


data.info()


# In[8]:


data.describe()


# In[9]:


data.isnull().sum()


# In[10]:


data.head()


# In[11]:


data.tail()


# In[12]:


data['ProdDate']=pd.to_datetime(data['ProdDate'])


# In[13]:


data


# In[ ]:


##100% availability of iron ore in geoth mine ,which can be extracted within 7 hours of mining using Komatsu Dump Truck is the 
#best choice to increase the production rate of iron .


# # second set

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("MM2.csv")


# In[3]:


df


# In[4]:


df['Date']=pd.to_datetime(df['Date'])


# In[5]:


df


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df


# In[ ]:


##B7 South blockid is better to use because 18250T ore is extracted by 2 blasts with 2100kg emulsion.


# # THIRD SET

# In[9]:


a=pd.read_csv("MM3.csv")


# In[10]:


a


# In[ ]:


#In surface mining, stripping ratio or strip ratio refers to the amount of waste (or overburden) 
#that must be removed to release a given ore quantity.


# In[14]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

a['TotalOre']=le.fit_transform(a['TotalOre'])


# In[15]:


a.info()


# In[17]:


a.plot(x='Equipment',y='TotalOre',kind='bar')


# # fourthset

# In[18]:


m4=pd.read_csv("mm4.csv")


# In[19]:


m4


# In[ ]:


#Truck1 is more efficient as it travelled 800km compared to Truck2


# # fifth set

# In[20]:


m5=pd.read_csv("MM6.csv")


# In[21]:


m5


# In[ ]:


#35T Dump Truck is better as breakdown hour is 0.


# # sixth set

# In[22]:


m7=pd.read_csv("MM7.csv")


# In[23]:


m7


# In[26]:


m7['ReportDate']=pd.to_datetime(m7['ReportDate'])


# In[27]:


m7


# In[ ]:


#PC200 CAT Excavator has 105kg load and total weight moved is 1312500kg.


# # seventh set

# In[24]:


m8=pd.read_csv("mm8.csv")


# In[25]:


m8


# In[28]:


m8['Date']=pd.to_datetime(m8['Date'])


# In[29]:


m8


# In[33]:


m8.plot(x='Equipment',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Equipment")
plt.ylabel("Target_TPH V/S Actual_TPH")
plt.title("Equipment v/s TPH")


# In[35]:


m8.plot(x='Operator',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Operator")
plt.ylabel("TPH")
plt.title("Operator vs TPH")


# In[36]:


m8.plot(x='Mine',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Mine")
plt.ylabel("TPH")
plt.title("Mine vs TPH")


# In[ ]:




