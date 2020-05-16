# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
for i in range(n):
    wt.append(0)
    tt.append(0)
    c.append(a[i])
sum=0
for i in range(n):
    d = min(c)
    if(i==0):
        sum += int(b[a.index(d)]) + int(d)
        wt[a.index(d)]=0
        tt[a.index(d)]=int(b[a.index(d)])
    else:
        wt[a.index(d)] = sum - int(d)
        tt[a.index(d)] = wt[a.index(d)]+int(b[a.index(d)])
        sum += int(b[a.index(d)])        
    #print(d,sum)
    c.pop(c.index(d))
print(wt,tt)
sum1=0
sum2=0
for i in range(n):
    sum1 += wt[i]
    sum2 += tt[i]
print('Total and average waiting time: ',sum1,',',sum1/n)
print('Total and average turnaround time: ',sum2,',',sum2/n)