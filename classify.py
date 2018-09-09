import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import time

path = input("enter the File name with .csv extension")
#print(path)

df=pd.read_csv(path)

df=df[:-195574]


df['status']=0

#computing the mean value for given dataframe
std=df[['value']].std()
#computing the mean value for dataframe
mean=df[['value']].mean()
threshold=mean+std

for index, row in df.iterrows():
    if (df.loc[index, 'value'] > threshold).bool() :
        df.loc[index,'status'] = '1'
        print(index)


new_df = df[df['status']!= 0]
del new_df['status']

new_df.to_csv('leaks.csv', index=False)