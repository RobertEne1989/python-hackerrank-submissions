'''
There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock, determine how many pairs of socks with
matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color.
The number of pairs is 2.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs

Input Format

The first line contains an integer n, the number of socks represented in ar.
The second line contains n space-separated integers,ar[i], the colors of the socks in the pile.

Constraints
1 <= n <= 100
1 <= ar[i] <= 100 where 0 <= i < n

'''

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # n = int(input().strip())
    # ar = input().strip().split()
    tot = 0
    d = {}

    for i in range(n):
        if ar[i] in d:
            d.pop(ar[i])
            tot += 1
        else:
            d[ar[i]] = 1

    return tot


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
