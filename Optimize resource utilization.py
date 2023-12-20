#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("mm.csv")


# In[9]:


data


# In[ ]:


##100% availability of iron ore in geoth mine ,which can be extracted within 7 hours of mining using Komatsu Dump Truck is the 
#best choice to increase the production rate of iron.


# # second set

# In[3]:


df=pd.read_csv("MM2.csv")


# In[10]:


df


# In[ ]:


##B7 South blockid is better to use because 18250T ore is extracted by 2 blasts with 2100kg emulsion.


# # third set

# In[4]:


DATA=pd.read_csv("MM3.csv")


# In[11]:


DATA


# In[ ]:


#In surface mining, stripping ratio or strip ratio refers to the amount of waste (or overburden) 
#that must be removed to release a given ore quantity.

#using scrapper , 1257T of iron ore is extracted in geoth mine with 0.16 stripping ratio.


# # fourth set

# In[5]:


DF=pd.read_csv("mm4.csv")


# In[12]:


DF


# In[ ]:


#Truck1 is more efficient as it travelled 800km compared to Truck2


# # fifth set

# In[6]:


dataframe=pd.read_csv("MM6.csv")


# In[13]:


dataframe


# In[ ]:


# countingthe the time the asset fails to the time you manage to get it up and running again. 
#35T Dump Truck is better as breakdown hour is 0.


# # sixth set

# In[7]:


DATAFRAME=pd.read_csv("MM7.csv")


# In[14]:


DATAFRAME


# In[ ]:


#PC200 CAT Excavator has 105kg load and total weight moved is 1312500kg.


# # seventh set

# In[8]:


frame=pd.read_csv("mm8.csv")


# In[15]:


frame


# In[ ]:


#Total petroleum hydrocarbons (TPH) is a term used to describe a large family of several hundred 
#chemical compounds that originally come from crude oil. Crude oil is used to make petroleum products,


# In[ ]:


#RP minerals and Reddy coal mine exceeded the target TPH and working hours for Reddy coal mine is 8 in Delhi .
#Hence Reddy coal mine is worth using truck.


# In[17]:


frame.plot(x='Mine',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Mine")
plt.ylabel("TPH")
plt.title("Mine vs TPH")


# In[ ]:




