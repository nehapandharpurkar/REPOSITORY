#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("annual_data.csv")


# In[3]:


df


# In[7]:


df=df.drop('SNA08TRANS',axis=1)


# In[6]:


df=df.drop('Descriptor',axis=1)


# In[9]:


df=df.drop('Inst_sector',axis=1)


# In[10]:


df


# In[11]:


df.info()


# In[12]:


df['Period']=pd.to_datetime(df['Period'])


# In[13]:


df


# In[15]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Period']=le.fit_transform(df['Period'])
df['Asset_liability_code']=le.fit_transform(df['Asset_liability_code'])
df.info()


# In[16]:


x=df.drop(columns=['Asset_liability_code'])
y=df['Inst_sector_code']


# In[17]:


from sklearn.model_selection import train_test_split


# In[18]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)


# In[19]:


from sklearn.tree import DecisionTreeClassifier
dt=DecisionTreeClassifier()
dt.fit(x_train,y_train)
y_pred=dt.predict(x_test)
y_pred


# In[20]:


from sklearn.metrics import *
confusion_matrix(y_test,y_pred)


# In[21]:


accuracy_score(y_test,y_pred)


# In[23]:


df


# In[24]:


plt.hist(df['Inst_sector_code'])


# In[28]:


x=df['Period']
y=df['Asset_liability_code']
plt.scatter(x,y)


# In[29]:


plt.bar(x,y)


# In[ ]:





# In[ ]:





# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


get_ipython().system('pip install prophet')


# In[4]:


df=pd.read_csv("annual_data.csv")


# In[5]:


df


# In[6]:


df['Period']=pd.to_datetime(df['Period'])


# In[7]:


df


# In[8]:


df.plot()


# In[9]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Asset_liability_code']=le.fit_transform(df['Asset_liability_code'])


# In[13]:


df=df.drop('Inst_sector',axis=1)


# In[14]:


df=df.drop('Descriptor',axis=1)


# In[15]:


df=df.drop('SNA08TRANS',axis=1)


# In[16]:


df.plot()


# In[17]:


# Test for rolling statistics
mean_log = df.rolling(window=12).mean() #rolling() --> Works for computing the moving statistical values
std_log = df.rolling(window=12).std()

# Each value in the rolling mean series is the average of the current value and the previous 11 values

plt.plot(df, color='blue', label='Original')  # Plotting for the whole dataset --> Blue
plt.plot(mean_log, color='red', label='Rolling Mean') # Plotting for rolling mean --> Red
plt.plot(std_log, color='black', label='Rolling Std') # Plotting for rolling std  --> Black
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation (Logarithmic Scale)')


# In[ ]:




