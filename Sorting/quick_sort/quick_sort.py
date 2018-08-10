# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 22:45:02 2018

@author: Aman Dubey"""

def swap(x,y):
    return y,x

def partition(A, start, end):
    pivot = A[end]
    pindex = start
    for i in range(start,end):
        if A[i]<=pivot:
            A[i],A[pindex] = swap(A[i],A[pindex])
            pindex = pindex+1
    A[pindex],A[end] = swap(A[pindex],A[end])
    return pindex

def sort(A,start,end):
    if start<end:
        pindex = partition(A,start, end)
        sort(A,start,pindex-1)
        sort(A,pindex+1,end)
    
x = [16, 14, 10, 8, 7, 3, 2, 4, 1]
start = 0
end = len(x)-1
sort(x,start,end)

print(x)