#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[32]:


df_flights = pd.read_csv ('~/Downloads/C1DC/Flights.csv')
df_tickets = pd.read_csv ('~/Downloads/C1DC/Tickets.csv')
df_ac = pd.read_csv ('~/Downloads/C1DC/ac.csv')


# Cleaning Missing Values

# See how many null values are in each columns

# In[33]:


df_flights.isnull().sum()


# In[34]:


df_tickets.isnull().sum()


# In[35]:


df_ac.isnull().sum()


# Drop rows with any null values

# In[36]:


df_na_flights=df_flights.dropna(how='any')
df_na_tickets=df_tickets.dropna(how='any')
df_na_ac=df_ac.dropna(how='any')


# See how many duplicates are in each data frame

# In[37]:


df_na_flights.duplicated().sum()


# In[38]:


df_na_tickets.duplicated().sum()


# In[39]:


df_na_ac.duplicated().sum()


# Looking at the rows that are duplciated

# In[40]:


df_na_flights[df_na_flights['TAIL_NUM'].duplicated()].head()


# In[41]:


df_na_tickets[df_na_tickets['ITIN_ID'].duplicated()].head()


# In[42]:


df_na_ac[df_na_ac['IATA_CODE'].duplicated()].head()


# Drop Duplicates in the data sets

# In[68]:


df_dd_flights=df_na_flights.drop_duplicates()
df_dd_tickets=df_na_tickets.drop_duplicates()
df_dd_ac=df_na_ac.drop_duplicates() 


# Drop Non-Numeric Rows

# In[69]:


df_dd_flights2 = df_dd_flights[pd.to_numeric(df_dd_flights['DEP_DELAY'], errors='coerce').notnull()]


# In[70]:


df_dd_flights3 = df_dd_flights[pd.to_numeric(df_dd_flights['ARR_DELAY'], errors='coerce').notnull()]


# In[71]:


df_dd_flights4 = df_dd_flights[pd.to_numeric(df_dd_flights['CANCELLED'], errors='coerce').notnull()]


# In[72]:


df_dd_flights5 = df_dd_flights[pd.to_numeric(df_dd_flights['AIR_TIME'], errors='coerce').notnull()]


# In[73]:


df_dd_flights6 = df_dd_flights[pd.to_numeric(df_dd_flights['DISTANCE'], errors='coerce').notnull()]


# In[74]:


df_dd_flights7 = df_dd_flights[pd.to_numeric(df_dd_flights['OCCUPANCY_RATE'], errors='coerce').notnull()]


# In[75]:


df_dd_flights7.head()


# Export to csv

# In[76]:


df_dd_flights7.to_csv('~/Downloads/C1DC/Clean_Flights.csv', index=False)
df_dd_tickets.to_csv('~/Downloads/C1DC/Clean_Tickets.csv',index=False)
df_dd_ac.to_csv('~/Downloads/C1DC/Clean_AC.csv',index=False)


# In[ ]:




