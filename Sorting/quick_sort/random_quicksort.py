# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 11:23:10 2018

@author: Aman Dubey
"""
import random

def swap(a,b):
    return b,a

def partition(x,start,end):
    pivot = x[end]
    pindex = start
    for i in range(start, end):
        if x[i] < pivot:
            x[i],x[pindex] = swap(x[i],x[pindex])
            pindex += 1
    x[pindex],x[end] = swap(x[pindex],x[end])
    return pindex

def randomized_partition(A, p, r):
    i = random.randint(p,r)
    A[r], A[i] = swap(A[r], A[i])
    return partition(A, p, r)

def randomized_quicksort(x,start,end):
    if start<end:
        pindex = randomized_partition(x, start, end)
        randomized_quicksort(x, start, pindex - 1)
        randomized_quicksort(x, pindex +1, end)
        
        
x = [16, 14, 10, 8, 7, 3, 2, 4, 1]
start = 0
end = len(x)-1
randomized_quicksort(x,start,end)

print(x)