#!/usr/bin/env python
# coding: utf-8

# <h1>Importation du DATA<h1>

# In[4]:


# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import re

# chargement et affichage des données
data = pd.read_csv('C:/Users/HP/Downloads/archive/bank_transactions.csv')
data.head(10)


# In[5]:


data.shape


# <h1>Missing values</h1>

# In[6]:


#valeurs manquantes
data.isna().sum()


# In[7]:


data.dropna(inplace=True)


# In[8]:


data.isna().sum()


# <h1>Duplicates<h1>

# In[9]:


#Showing how many duplicated rows for the whole dataset
data.duplicated().sum()


# In[10]:


#return a True if the row is duplicated and False if not
data.duplicated()


# In[11]:


#removes all duplicated rows
data.drop_duplicates(inplace=True)


# In[12]:


#
data.duplicated()


# In[13]:


data.shape


# In[14]:


data.duplicated().sum()


# In[ ]:





# In[15]:


data.describe()


# In[16]:


data.isna().sum().sum()


# In[17]:


##import libraries
import matplotlib.pyplot as plt 
import seaborn as sns


# In[18]:


#made a copy of data
df1 = data
#calcule quartile and IQR
Q1 = data["CustAccountBalance"].quantile(0.25)
Q3 = data["CustAccountBalance"].quantile(0.75)
IQR = Q3 - Q1
#find upper and lower limits
upper_limit = Q3 + 1.5 * IQR 
lower_limit = Q1 - 1.5 * IQR

upper_limit , lower_limit


# In[19]:


sns.boxplot(df1["CustAccountBalance"])


# In[20]:


##capping
df1[df1["CustAccountBalance"] < lower_limit] = lower_limit
df1[df1["CustAccountBalance"] > upper_limit] = upper_limit


# In[21]:


sns.boxplot(df1["CustAccountBalance"])


# In[22]:


#made a copy of data
df1 = data
#calcule quartile and IQR
Q1 = data["TransactionAmount (INR)"].quantile(0.25)
Q3 = data["TransactionAmount (INR)"].quantile(0.75)
IQR = Q3 - Q1
#find upper and lower limits
upper_limit = Q3 + 1.5 * IQR 
lower_limit = Q1 - 1.5 * IQR

upper_limit , lower_limit


# In[23]:


sns.boxplot(df1["TransactionAmount (INR)"])


# In[24]:


df1[df1["TransactionAmount (INR)"] < lower_limit] = lower_limit
df1[df1["TransactionAmount (INR)"] > upper_limit] = upper_limit


# In[25]:


sns.boxplot(df1["TransactionAmount (INR)"])


# In[26]:


#made a copy of data
df1 = data
#calcule quartile and IQR
Q1 = data["TransactionTime"].quantile(0.25)
Q3 = data["TransactionTime"].quantile(0.75)
IQR = Q3 - Q1
#find upper and lower limits
upper_limit = Q3 + 1.5 * IQR 
lower_limit = Q1 - 1.5 * IQR

upper_limit , lower_limit


# In[27]:


sns.boxplot(df1["TransactionTime"])


# In[28]:


df1[df1["TransactionTime"] < lower_limit] = lower_limit
df1[df1["TransactionTime"] > upper_limit] = upper_limit


# In[29]:


sns.boxplot(df1["TransactionTime"])


# In[34]:


def plot_boxplot(data,ft):
    data.boxplot(column=[ft])
    plt.grid(False)
    plt.show()


# In[35]:


plot_boxplot(data,"TransactionAmount (INR)")

