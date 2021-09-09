'''
Given three integers, t1, t2, and n, compute and print the n'th term of a modified Fibonacci sequence.

Example
t1 = 0
t2 = 1
n = 6

t3 = 0 + 1^2 = 1
t4 = 1 + 1^2 = 2
t5 = 1 + 2^2 = 5
t6 = 2 + 5^2 = 27
Return 27.

Function Description

Complete the fibonacciModified function in the editor below. It must return the n'th number in the sequence.

fibonacciModified has the following parameter(s):

int t1: an integer
int t2: an integer
int n: the iteration to report

Returns

int: the n'th number in the sequence
Note: The value of t[n] may far exceed the range of a 64-bit integer. Many submission languages have libraries
that can handle such large results but, for those that don't (e.g., C++), you will need to compensate for
the size of the result.

Input Format

A single line of three space-separated integers, the values of t1, t2, and n.

Constraints
0 <= t1,t2 <= 2
3 <= n <= 20
t(n) may far exceed the range of a 64-bit integer.
'''

import math
import os
import random
import re
import sys


def fibonacciModified(t1, t2, n):
    for i in range(n - 2):
        n = t1 + (t2 ** 2)
        t1 = t2
        t2 = n
    return t2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
