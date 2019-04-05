# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 09:42:01 2018

@author: Aman Dubey
"""
def insertion_sort_merge(y,low, mid, high):
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


def sort(y,low, high):
    if low < high: 
        mid = (low+high)//2 # finding the center of the array   
        sort(y,low,mid)       # Recursive call for the sort first half of the array
        sort(y,mid+1,high)    # Recursive call for sort the first half of the array
        insertion_sort_merge(y,low,mid,high)  # calling the insertion sort function to sort and merge the array in a single array
        

y = [3,2,6,5,4,1]
low = 0
high = len(y)
sort(y,low,high)
print(y)
