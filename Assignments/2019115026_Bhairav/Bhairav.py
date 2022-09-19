#!/usr/bin/env python
# coding: utf-8

# # Basic Python

# ## 1. Split this string

# In[1]:


s = "Hello I'm Bhairav AJ"


# In[2]:


s.split()


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[4]:


place = "GUINDY"
distance = 35


# In[5]:


print("The distance of {} from my house is {} kilometers.".format(place,distance))


# ## 3. In this nest dictionary grab the word "hello"

# In[ ]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[ ]:


print(d['k1'][3]['tricky'][3]['target'][3])


# # Numpy

# In[18]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[19]:


np.zeros(10)


# In[20]:


np.ones(10) * 5


# ## 5. Create an array of all the even integers from 20 to 35

# In[ ]:


np.arange(20,35,2)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[22]:


np.arange(0,9).reshape(3,3)


# ## 7. Concatinate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[ ]:


a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b),axis = 0)
print(c)


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[28]:


import pandas as pd
df = pd.DataFrame({"Name":['Praveen','Chandra','Suriya'],"Age":[21,21,20]})


# In[27]:


print(df)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[ ]:


np.arange('2023-01-01','2023-02-10',dtype='datetime64[D]')


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[ ]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[ ]:


df = pd.DataFrame(lists)
print(df)


# In[ ]:




