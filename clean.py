import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import csv
import string
from collections import Counter

import collections, re

import random
from random import randint


import pandas as pd

path = input("enter the File name with .csv extension")
print(path)





#path='S4_RelativePression.csv'       #getting file

with open(path,newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]

i=0
j=0
arr=[]
for d in data:
    j=0
    sublist=[]
    if i==0:
        sublist.append('date')
        sublist.append('time')
        sublist.append('value')
        i+=1
        continue
    for cell in d:
        if j%2==0:
            try:
                temp=cell.split()
                date=temp[0]
                sublist.append(date)
                time=temp[1]
                lastdigit=time.split(';')
                time=lastdigit[0]
                sublist.append(time)
                last=lastdigit[1]
            except:
                sublist=[]
                continue
        else:
            try:
                cell=cell.split(';')[0]
                value=last+'.'+cell
                sublist.append(value)
            except:
                sublist=[]
                continue
        j+=1
    if sublist!=[]:
        arr.append(sublist)
    i+=1

with open('processed_file.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['date','time','value'])
    w.writerows(arr)


