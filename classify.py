import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import time

path = input("Enter the File name with .csv extension, default : 'data/clean-out.csv'.")
if path == "":
    path = "data/clean-out.csv"
print(path)

df=pd.read_csv(path)

df['status']=0

#computing the mean value for given dataframe
std=df[['value']].std()
print ('std %.2f' % std)
#computing the mean value for dataframe
mean=df[['value']].mean()
print ('mean %.2f' % mean)
threshold=mean+std
print ('threshold  %.2f' % threshold)

for index, row in df.iterrows():
    if (df.loc[index, 'value'] > threshold).bool() :
        df.loc[index,'status'] = '1'
        #print(index)


new_df = df[df['status']!= 0]
del new_df['status']

new_df.to_csv('data/classify-out.csv', index=False)
print('data/classify-out.csv')