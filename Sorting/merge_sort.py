45# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 08:47:13 2018

@author: Aman Dubey
"""

y = [6,5,4,3,2,1]

def merge(left,right,y):
    i=0
    j=0
    k=0
    nl = len(left)
    nr = len(right)
    while(i<nl and j<nr):
        if left[i] <= right[j]:
            y[k] = left[i]
            i+=1
        else:
            y[k] = right[j]
            j+=1            
        k+=1
    while(i<nl):
        y[k] = left[i]
        i +=1
        k+=1
    while(j<nr):
        y[k] = right[j]
        j+=1
        k+=1

def mergesort(y):
    n = len(y)
    if n<2:
        return
    mid = (n+1)//2
    left = []
    right = []
    for i in range(0,mid):
        left.append(y[i])
    for j in range(mid, n):
        right.append(y[j])
    
    mergesort(left)
    mergesort(right)
    merge(left,right,y)

mergesort(y)
print(y)