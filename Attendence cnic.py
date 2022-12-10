#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install pycaret  #https://github.com/pycaret/pycaret
#conda create -n pycaret python=3.8


# In[6]:


from pycaret.datasets import get_data 

titanic_df = get_data("titanic")


# In[8]:


import re 
import pandas as pd
import numpy as np

x = """
zain abidi2:58 PM
4250119167549
You2:59 PM
4210129511133
Muneeb Ahmed2:59 PM
42101 8342718 3
Muhammad Ayaz3:00 PM
4410242997959
Arsalan Ahmed3:01 PM
42201-6535195-7
Sumayya Kamran EB20_125 (EB20102125)3:03 PM
4250106544552
Dewan S Khan3:05 PM
import streamlit as st
import pandas as pd
import geopandas as gpd

st.title("Streamlit UBL karachi Top 20 Branches Plot on Streamlit Geo Graph")

data = pd.read_csv("ubl.csv")

data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.Longitude, data.Latitude))

st.write("This graph shows the top 20 UBL branches in Karachi")

st.write("")

st.map(data)
Syed Usama Shahzad3:07 PM
42101-3416307-9
Dewan S Khan3:07 PM
4220105630741
taimoor qureshi3:09 PM
4240179641627
Arsalan Risalat3:10 PM
4220124812817
Muhammad Rohan3:13 PM
4210116966995
Muneeb Ahmed3:13 PM
42101 8342718 3
Aqeel Mehdi3:16 PM
Sir ap apna mic mute kardain
Bilal Ahmed3:20 PM
4210120075463
Dewan S Khan3:21 PM
4220105630741
Faiza Asad3:23 PM
4200052746960
syed daniyal3:29 PM
4250189782769
Dewan S Khan3:29 PM
4220105630741
Hassan Khan3:30 PM
4240160019477
muhammad Ajmal Hassan3:40 PM
4220131265069
Tariq Mehmood3:42 PM
4220104505899
usman ahmad3:43 PM
4220113316709
Nofil Ahmed3:46 PM
4210175076663
Khawar Masood3:49 PM
Syed Khawar Masood Naqvi
42101-4113797-7
Dewan S Khan3:49 PM
4220105630741
Syed Sajjad Raxa3:50 PM
4220143471143
Khawar Masood3:50 PM
4240114707349
Munir Ali3:50 PM
4220101410369
Nazneen Akram3:50 PM
4210145447712
Muhammad Atique Qayyum3:50 PM
4220140225263
Syed Masroor Ali (Masroor)3:51 PM
42401-1880106-5
42201-2286846-7
HAREEM RIZVI3:55 PM
42101-3311570-4
Dewan S Khan3:58 PM
4220105630741
Zeeshan Naqvi3:59 PM
4210151751811
Mohsin Kanani3:59 PM
4230108335683
Malik Humza3:59 PM
4240105171159
You4:01 PM
4210129511133
Syed Usama Shahzad4:01 PM
42101-3416307-9
Wasiq Gt4:01 PM
4250104502069
Dewan S Khan4:01 PM
4220105630741
Zeeshan Javed4:01 PM
4230189725317
Afnan Ali4:01 PM
4210146436547
Zareen Fatima4:01 PM
3520269403788
Aqeel Mehdi4:01 PM
4220105436681
Muhammad Ayaz4:01 PM
4410242997959
Hassan Ahmed4:01 PM
4220156089133
Tabassum Ali4:01 PM
4230123126547
Faiza Asad4:01 PM
4200052746960


"""

cnic =pd.DataFrame(list(set(re.findall("\d{13}",x))),columns=['CNIC'])
print(len(cnic))
cnic


# In[ ]:




