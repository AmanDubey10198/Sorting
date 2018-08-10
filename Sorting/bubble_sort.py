# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:19:01 2018

@author: Aman Dubey
"""

y = [3,2,5,6,4,1]

def bubble_sort(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            while x[j]>x[j+1]:
                temp = x[j+1]
                x[j+1] = x[j]
                x[j] = temp
                
bubble_sort(y)
print(y)