# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 23:15:47 2018

@author: Aman Dubey
"""

x = [2,4,5,6,1,3]

#Insertion sort
def insertion_sort(y):
    for i in range(1,len(y)):
    #make a key
        key = y[i]
        j = i-1
    #compare key from previous values
        while j>-1:
            if key < y[j]:
                y[j+1] = y[j]
                j -=1
            else:
                break
        y[j + 1] = key
    return y

insertion_sort(x)
print(x)

