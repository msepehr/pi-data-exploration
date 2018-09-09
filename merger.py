import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import time
import calendar

path = input("enter the DataFile name with .csv extension")
print(path)


df=pd.read_csv(path)

add = input("enter the additional datafile name with .csv extension")
print(path)

ad_data=pd.read_csv(add)

for index, row in ad_data.iterrows():
    df=df.append(ad_data.loc[index])
    
df = df.reset_index(drop=True)
df['day']=0
df['month']=''
df['year']=0



for index, row in df.iterrows():
    time_str= df.loc[index].date

    day, month, year = time_str.split('-')

    df.loc[index,'day']=int(day)
    df.loc[index,'month']=(month)
    df.loc[index,'year']=int(year)
    

df.drop_duplicates( subset=['date', 'time', 'value', 'day', 'month'], keep=False)

df=df.sort_values('time')
df=df.sort_values('day')
df=df.sort_values('month')
df=df.sort_values('year')

del df['month']
del df['year']
del df['day']

df.to_csv(path, index=False)