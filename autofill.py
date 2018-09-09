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

newdf=df
s1=df.loc[0].time
s2=df.loc[1].time
FMT = '%H:%M:%S'
tdelta = (datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT))*2

w1= df.loc[0].time
w2= df.loc[1].time
h1, m1, s1 = w1.split(':')
h2, m2, s2 = w2.split(':')

t1=int(h1) * 3600 + int(m1) * 60 +int(s1)
t2=int(h2) * 3600 + int(m2) * 60 +int(s2)

interval=int(m2)-int(m1)
interval


try:
    from itertools import product
except ImportError:
    def product(*seqs):
        if len(seqs) == 2:
            for s1 in seqs[0]:
                for s2 in seqs[1]:
                    yield (s1,s2)
        else:
            for s in seqs[0]:
                for p in product(*seqs[1:]):
                    yield (s,) + p

hhmmss = {}
i = 0
for (h,m,s) in product(range(24),range(60),range(60)):
    
    hhmmss[i] = "%02d:%02d:%02d" % (h,m,s)
    i += 1
    

count=0


counter=0
for index, row in df.iterrows():
    print(index)
    if(index>0):
        w1= df.loc[index].time
        
        h1, m1, s1 = w1.split(':')

        w2= df.loc[index-1].time
        
        h2, m2, s2 = w2.split(':')

        current_hour=int(h1)
        prev_hour=int(h2)
        current_min=int(m1)
        prev_min=int(m2)

        if(prev_min>current_min):
            
            current_min=current_min+60

        if(current_min-prev_min == interval):
            print('fine')
        else:
            prev_min=prev_min+interval
            prev_min=prev_min % 60
             
            strin= str(prev_hour)+ ':'+str(prev_min)+ ':'+'00'        
            newdf.loc[counter,'date'] = df.loc[index,'date'] 
            newdf.loc[counter,'time'] = strin
            newdf.loc[counter,'value'] = -1
            counter=counter+1

           



newdf = newdf[newdf['value']== -1]

newdf.to_csv('data/autofill-out.csv', index=False)
print('data/autofill-out.csv')