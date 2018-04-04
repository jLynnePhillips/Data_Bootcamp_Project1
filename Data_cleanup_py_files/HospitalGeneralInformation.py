
# coding: utf-8

# In[1]:


import pandas as pd 


# In[7]:


# df = pd.read_csv("Hospital General Information.csv")

df = pd.read_csv("Hospital General Information.csv",encoding='latin-1')


# In[8]:


df.head()


# In[11]:


CA_DF = df[df["State"] =="CA"]


# In[12]:


CA_DF


# In[16]:


CA_DF.keys()


# In[20]:


CA_DF.drop(['City','ZIP Code','Phone Number'], axis = 1)

