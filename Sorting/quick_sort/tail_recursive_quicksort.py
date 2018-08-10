# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


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

def tail_recursive_quicksort(A, start, end):
    while start < end:
        q = partition(A, start, end)
        print(A)
        tail_recursive_quicksort(A,start,q - 1)
        start = q + 1
    
x = [7, 4, 2, 3, 9, 10, 7, 6]
start = 0
end = len(x)-1
tail_recursive_quicksort(x,start,end)

print(x)