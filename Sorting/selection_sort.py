# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 21:53:22 2018

@author: Aman Dubey
"""

def selection_sort(X):
    
    for i in range(len(X)-1):
        imin = i
        for j in range(i+1, len(X)):
            if X[imin]>X[j]:
                imin = j
        temp = X[i]
        X[i] = X[imin]
        X[imin] = temp
    
    return X

import numpy as np
  
x = np.random.randn(10)

y = selection_sort(x)

print(y)