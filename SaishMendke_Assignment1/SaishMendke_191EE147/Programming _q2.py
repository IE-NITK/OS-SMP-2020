# -*- coding: utf-8 -*-
"""
Created on Sat May 16 01:30:48 2020

@author: Saish Mendke
"""

print('Enter n: ')
n = int(input())
print("Enter the arrival time: ")
a = input()
a = a.split(' ')
print('Burst time:')
b = input()
b = b.split(' ')
wt=[]
tt=[]
c=[]
e=[]
d=0
sum1=0
sum2=0
for i in range(n):
    wt.append(0)
    tt.append(0)
    c.append(b[i])
    e.append(a[i])
sum3=int(min(a))
for i in range(n):
    k=max(c)
    for j in range(len(c)):
        if(int(e[j])<=sum3 and int(c[j])<=int(k)):
            d=c[j]
            k=c[j]
    if(i==0):
        sum3 += int(b[b.index(d)])
        wt[b.index(d)]=0
        tt[b.index(d)]=int(b[b.index(d)])
    else:
        wt[b.index(d)] = sum3 - int(a[b.index(d)])
        tt[b.index(d)] = wt[b.index(d)]+int(b[b.index(d)])
        sum3 += int(b[b.index(d)]) 
    e.pop(c.index(d))
    c.pop(c.index(d))
for i in range(n):
    sum1 += wt[i]
    sum2 += tt[i]
print('Total and average waiting time: ',sum1,',',sum1/n)
print('Total and average turnaround time: ',sum2,',',sum2/n)

    