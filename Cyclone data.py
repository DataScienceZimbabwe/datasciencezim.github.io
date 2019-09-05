
# coding: utf-8

# In[155]:


import pandas as pd
import numpy as np
import random


# In[156]:


data = pd.DataFrame(columns = ['Cyclone Id','City','Date','Temperature','Latitude','Longitude', 'Wind','Altitude','Magnitude'], index = np.arange(100))


# In[157]:


data['Cyclone Id'] = list(range(100))
cities = ['Chimanimani', 'Mutare', 'Buhera', 'Chipinge', 'Binga', 'Harare']
data['City'] = random.sample(cities,5)*20
dates = pd.date_range(start='1900-01-01', periods = 100, freq='Y')
data['Date'] = np.array(dates)
data['Temperature'] = np.random.randint(5,40,100)
data['Latitude'] = np.random.randint(18,60,100)
data['Longitude'] = np.random.randint(18,60,100)
data['Wind'] = np.random.randint(0,360,100)
data['Altitude'] = np.random.randint(1000,5000,100)
data['Magnitude'] = np.random.randint(1,5,100)


# In[158]:


data.head()


# In[162]:


Cyclone_Data = data.to_csv('data.csv')

