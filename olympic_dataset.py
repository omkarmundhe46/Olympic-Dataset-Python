# -*- coding: utf-8 -*-
"""Olympic Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YeqLCNNQCVqdMy2SLtz4LVa8hCxB9mPg
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import re

"""reading dataset"""

athlete = pd.read_csv("/content/drive/MyDrive/athlete_events.csv")
noc = pd.read_csv("/content/drive/MyDrive/noc_regions.csv")

ath = athlete.copy()
nat = noc.copy()

"""DATA EXPLORATION"""

ath.head()

ath.info()

ath.describe()

ath.shape

ath.isnull().sum()

"""DATA CLEANING & MANIPULATION"""

at = ath.merge(nat,how="left",on="NOC")

region_col = ath['NOC'].map(nat.set_index('NOC')['region'])
ath.insert(7,'region',region_col)

ath

# drop the column "NOC" from "ath"
ath.drop("NOC", inplace = True, axis= 1)

ath

"""Handling the null values in column "Age, "Height,"Weight by mean of the respective columns"""

ath['Age'].fillna(ath.Age.mean(),inplace=True)
ath['Height'].fillna(ath.Height.mean(),inplace=True)
ath['Weight'].fillna(ath.Weight.mean(),inplace=True)

ath

ath.iloc[[147]]

"""list out all the values of region column where values are null"""

ath[ath.region.isna()]

nat.where(nat["region"]=="singapur")

"""Handling the null values in column "Medel"
"""

ath['Medal'].nunique()     # categories

ath['Medal'].unique()

ath['Medal'].value_counts()

ath['Medal'].replace([np.nan],[0],inplace=True)

ath.head()

ath['Medal'].replace({'Gold': 1, 'Silver': 2, 'Bronze': 3}, inplace=True)

ath

ath['Medal'].value_counts()

ath.Medal.astype(int)

ath.info()

"""dropping the region and games columns"""

ath.drop(['region','Games'],axis=1,inplace=True)

ath.head(1)

"""remove the unwanted phrases from "Event" column"""

for i,j in zip(ath.Sport,range(len(ath.Event))):
  ath.Event[j]=re.sub(f"{i}\s","",ath.Event[j])

ath.head(2)

"""EXPORTATION OF THE DATAFRAME"""

# ath.to_json("athletes_dataset.json")

# ath.to_csv("athletes_dataset.csv")

"""DATA ANALYSIS

show the relation between height & weight
"""

x = ath.Height
y = ath.Weight
plt.scatter(x,y)
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

"""find out how many males and females had participating in olympic during 1896 to 2016."""

at['Sex'].value_counts().plot.bar(at['Sex'])

"""how many male has been participating in summer and winter olympic"""

import plotly.express as px

# fig = px.histogram(ath,x=ath.Season,color=ath.Sex,barmode = "group")
fig = px.histogram(ath,x=ath.Season,color=ath.Sex,barmode = "group",color_discrete_map={"M":"#BA55D3","F":"Red"})
fig.show()

"""top 5 country who have most medal"""

ath.groupby('Team')['Medal'].sum().sort_values(ascending=False).head(5)

fig = px.histogram(ath.Medal,x = ath.Team)
fig.show()

fig = px.histogram(ath[ath['Sex']=='F ']['Sex'],x=ath.Year)
fig.show()

