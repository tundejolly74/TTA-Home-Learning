#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Create a 1D array of numbers from 0 to9
import numpy as np
a =np.arange(0,10)
print(a)


# In[22]:


#Create a 3×3 NumPy array of allBoolean value Trues
arr=np.array(True)
allBoolean=np.repeat(arr,3, axis=0)
print(allBoolean)


# In[29]:


#Create a 3x3 Numpy array of allBoolean value Trues
bool_arr = np.ones((3,3), dtype=bool)
print(bool_arr)


# In[47]:


#Extract all odd numbers from array of 1-10
arr =np.array([1,2,3,4,5,6,7,8,9,10])

print(arr[0::2])


# In[55]:


#Replace all odd numbers in an array of 1-10 with the value -1
arr = np.array([1,2,3,4,5,6,7,8,9,10])
arr[0::2]=-1

print(arr)


# In[5]:


#Convert a 1D array to a 2D array with 2rows
import numpy as np
array = np.array([3,4,5,6,7,8])
array_2d = np.reshape(array,(2,3))
print(array_2d)


# In[19]:


#Create two arrays a and b, stack these two arrays vertically use the  np.dot and np.sum to calculatetotals
a = np.arange(1,10).reshape(3,3)
b = np.arange(2,11).reshape(3,3)
print(a)

print(b)


# In[20]:


c = np.dot(a,b)
print(c)


# In[21]:


d = np.sum(c)
print(d)


# In[22]:


#Create the following pattern without hardcoding. Use only NumPy  functions
a = np.array([1,2,3])
np.r_[np.repeat(a, 3), np.tile(a, 3)]


# In[26]:


#In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) –remove allrepeating  items present in arrayb
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7,8,9])
c = np.setdiff1d(b, a)
print(c)


# In[35]:


#Get all items between 3and 7from a and b and sum themtogether
d = np.array([3,4,5,4,5,6,7])
sum=np.sum(d)
print(sum)

