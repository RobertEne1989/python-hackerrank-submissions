'''
Task

You are given a 2-D array with dimensions NxM.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format

The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.
'''


import numpy as np



n, m = map(int, input().split())
arr = []
for i in range(int(n)):
    array = list(map(int, input().split()))
    arr.append(array)
my_array = np.array(arr)
result = np.min(my_array, axis = 1)
print(max(result))
