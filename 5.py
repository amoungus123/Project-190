#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataframe = pd.read_csv('country_satellites.csv')

top_5 = dataframe.head(5)
print(top_5)
name = top_5['Country/Organization Name']
number = top_5['Satellites In Orbit']

plt.xlabel("Country/Organization Name")
#plt.xticks(rotation='vertical')
plt.ylabel("Satellites In Orbit")

label = name
value = number
plt.bar(label, value,width=0.4, color=('red','blue','green','purple','yellow'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




