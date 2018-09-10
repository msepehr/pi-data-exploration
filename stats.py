import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime
import time
import calendar

path = input("Enter the File name with .csv extension, default : 'data/clean-out.csv'.")
if path == "":
    path = "data/clean-out.csv"
print(path)

df=pd.read_csv(path)


stat = pd.DataFrame(columns=['date','hour','percentage'])

#to check the limit of the dataset

df2 = df.head(100)

temp=df2.loc[0].time

hh, mm, ss = temp.split(':')
correctTime=int(hh) * 3600 + int(mm) * 60 +int(ss)
temp_hour=int(hh)
print('temp_hour %s' % (temp))
index=0
check=True
limit=0
for index, row in df2.iterrows():
    w1= df.loc[index].time 
    h1, m1, s1 = w1.split(':')
    t1=int(h1) * 3600 + int(m1) * 60 +int(s1)
    current= int(h1)
    if(check==True):
        if(temp_hour==current):
            limit=limit+1
        else:
            check=False
    


#date to gather initial date 
time_str= df.loc[index].date

day, month, year = time_str.split('/')
initial_day=int(day)
currenr_day=int(day)
initial_date=df.loc[index].date


#initial time
temp=df.loc[0].time

hh, mm, ss = temp.split(':')
initial_hour=int(hh)
current_hour=int(hh)


hour_count=0
counter=0


for index, row in df.iterrows():
    #print(index)
    
    #checking the current row time
    w1= df.loc[index].time 
    h1, m1, s1 = w1.split(':')
    current_hour= int(h1)
   
    
    #checking the current day
    time_str= df.loc[index].date
    day, month, year = time_str.split('/')
    current_day=int(day)
    
    per=(hour_count/limit)*100
    if(current_hour!=initial_hour):
        if(currenr_day!=initial_day):
            stat = stat.append({'date':initial_date , 'hour': initial_hour, 'percentage': per},ignore_index=True)
            initial_date=df.loc[index].date
        else:
            stat = stat.append({'date':time_str , 'hour': initial_hour, 'percentage': per},ignore_index=True)
        #will enter the value in the dataframe
        initial_hour=current_hour
        per=0
        hour_count=0                
    if(current_hour==initial_hour):
        hour_count=hour_count+1
    



stat.to_csv('data/stats-out.csv', index=False)
print('data/stats-out.csv')