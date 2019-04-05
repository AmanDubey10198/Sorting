# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 23:21:42 2018

@author: Aman Dubey
"""
# initializing an array
A = [2,5,3,0,2,3,0,1,7,6,4,5,3]

k = max(A) # Taking the maximum of the array so that our auxillary array will be of size k

n = len(A)

# Creating and initializing the auxillary array C with value 0
C = []
for i in range(k+1):
    C.append(0)
    
# calculating and storing the frequency of each element of array in array C.
for j in range(n):
    C[A[j]] += 1

# Now storing the cumulative frequency in C.
for k in range(1,k+1):
    C[k] = C[k] + C[k-1]

# Creating and initilaizing a new array with value 0.
B = []
for i in range(n):
    B.append(0)

# iterate the array in reverse because the position at which we are going to insert in 'B' is taken from the value of 'C' at index
# "A[l] -1" by doing this we make the sorting technique **INPLACE** 
for l in range(n-1,- 1, -1):
    B[C[A[l]]-1] = A[l]
    C[A[l]] = C[A[l]] - 1
    
print(B)
