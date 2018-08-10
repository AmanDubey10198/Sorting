# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 12:11:58 2018

@author: Aman Dubey
"""
def swap(a,b):
    return b,a

def hoare_partition(A,p,r):
    x = A[p]
    i = p
    j = r
    while True:
        while A[j]<=x and j>p:
            j=j-1
        while A[i]>=x and i<r:
            i += 1
        if i<j:
            A[i],A[j] = swap(A[i],A[j])
        else: 
            return j
    return

def quicksort(x,start,end):
    if start<end:
        pindex = hoare_partition(x, start, end)
        quicksort(x, start, pindex - 1)
        quicksort(x, pindex +1, end)
        
        
x = [16, 14, 10, 8, 7, 3, 2, 4, 1]
start = 0
end = len(x)-1
quicksort(x,start,end)

print(x)