# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:21:42 2018

@author: Aman Dubey
"""

A = [2,5,3,0,2,3,0,1,7,6,4,5,3]
k = max(A)
n = len(A)
C = []

for i in range(k+1):
    C.append(0)

for j in range(n):
    C[A[j]] += 1

for k in range(1,k+1):
    C[k] = C[k] + C[k-1]

B = []

for i in range(n):
    B.append(0)

for l in range(n-1,- 1, -1):
    B[C[A[l]]-1] = A[l]
    C[A[l]] = C[A[l]] - 1
    
print(B)
