#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
holiday = pd.read_csv("holiday_destination.csv")
print(holiday)


# In[41]:


holiday.shape


# In[3]:


print(holiday.iloc[3:8])


# In[20]:


holiday['Hotel numbers']


# In[31]:


holiday["Hotel numbers"].tolist()


# In[44]:


holiday["Destination"].min()


# In[45]:


holiday["Destination"].max()


# In[53]:


holiday.mean()


# In[57]:


myfilter = holiday["Feedback Score"] > 8
print(myfilter)


# In[59]:


mysecond_filter = holiday["Feedback Score"] < 2
print(mysecond_filter)


# In[ ]:




