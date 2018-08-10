# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:42:01 2018

@author: Aman Dubey
"""
y = [3,2,6,5,4,1]
def insertion_sort_merge(low, mid, high):
    for i in range(1,high):
        key = y[i]
        j = i-1
        while j>-1:
            if key < y[j]:
                y[j+1] = y[j]
                j -=1
            else:
                break
        y[j + 1] = key


def sort(low, high):
    if low < high:
        mid = (low+high)//2
        sort(low,mid)
        sort(mid+1,high)
        insertion_sort_merge(low,mid,high)
        

low = 0
high = len(y)
sort(low,high)
print(y)