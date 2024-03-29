# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aKXXg-CkHs88s8ocz2eZTpUO-a65C8Cy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("/content/drive/MyDrive/dataset/titanic/Titanic-Dataset.csv")
df

df.head(10)
df.shape
df.describe()

df['Survived'].value_counts()

sns.countplot(x=df['Survived'],hue=df['Pclass'])

df['Sex']

sns.countplot(x=df['Sex'],hue=df['Survived'])

df.groupby('Sex')[['Survived']].mean()

from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
df['Sex']=labelencoder.fit_transform(df['Sex'])
df.head()

df['Sex'],df['Survived']

df.isna().sum()

df=df.drop(['Age'],axis=1)

df_final=df
df_final.head(10)

x=df[['Pclass','Sex']]
y=df['Survived']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LogisticRegression
log=LogisticRegression(random_state=0)
log.fit(x_train,y_train)

pred=print(log.predict(x_test))

print(y_test)

import warnings
warnings.filterwarnings("ignore")
res=log.predict([[2,1]])
if(res==0):
  print("sorry! Not survived")
else:
  print("survived")