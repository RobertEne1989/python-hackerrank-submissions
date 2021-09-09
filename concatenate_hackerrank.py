'''
Task

You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column).
Your task is to concatenate the arrays along axis 0.

Input Format

The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size (N + M) x P.
'''


import numpy

n, m, p = map(int, input().split())

s1 = " ".join(input() for _ in range(n))
m1 = numpy.array(s1.split(), int)
m1.shape = (n, p)

s2 = " ".join(input() for _ in range(m))
m2 = numpy.array(s2.split(), int)
m2.shape = (m, p)

print(numpy.concatenate((m1, m2), axis=0))
