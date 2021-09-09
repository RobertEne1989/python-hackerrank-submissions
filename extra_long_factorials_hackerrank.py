'''
e factorial of the integer n, written n!, is defined as:
    n! = n x (n-1) x (n-2) x ... x 3 x 2 x 1


Calculate and print the factorial of a given integer.

For example, if n = 30, we calculate 30 x 29 x 28 x ... x 2 x 1 and get 265252859812191058636308480000000.

Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

n: an integer

Note: Factorials of n>20 can't be stored even in a 64 bit long long variable. Big integers must be used for such
calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional
code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

Input Format

Input consists of a single integer n

Constraints
1 <= n <= 100

Output Format

Print the factorial of n.
'''


import math
import os
import random
import re
import sys


def extraLongFactorials(n):
    k = n
    for i in range(1, n):
        k = k * (n - i)
    return print(k)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
