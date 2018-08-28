
# coding: utf-8

# In[4]:

import pandas as pd
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# import data
data = pd.read_csv("C:/Users/Sam/Documents/Course_Sem2/Data Mining/Python/HW1/abalone.csv")

# a. What are the column names of the dataset?
list(data)


# In[5]:

# b. How many observations (i.e. rows) are in this data frame?
data.shape[0]


# In[6]:

# c. Print the first 4 lines from the dataset. What are the values of feature rings of the printed observations?
data.head(4)
data.head(4)["Rings"]


# In[7]:

# d. Extract the last 3 rows of the data frame. What is the weight of these abalones?
data.tail(3)
data.tail(3)["Weight"]


# In[8]:

# e. What is the value of diameter in the row 755?
data.at[754,'Diameter']


# In[9]:

# f. How many missing values are in the height column?
data.Height.isnull().sum()


# In[10]:

# g. What is the mean of the height column? Exclude missing values from this calculation.
data.Height.mean()


# In[19]:

# h. Extract the subset of rows of the data frame where gender is M and weight values are below 0.75. What is the mean of diameter in this subset?

datasubset = data[(data["Gender"] == 'M') & (data["Weight"] < 0.75)]
datasubset
datasubset.Diameter.mean()


# In[14]:

# i. What is the most frequent rings value?
dataRing = data.dropna(subset=['Rings'])
dataRing['Rings'].value_counts().idxmax()


# In[17]:

# j. What is the minimum of length when rings is equal to 18?
dataRing18 = data[(data["Rings"] == 18)]
dataRing18.Length.min()




