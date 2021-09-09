'''
There is a string, s, of lowercase English letters that is repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

Example
s = 'abcac'
n = 10

The substring we consider is abcacabcac, the first 10 characters of the infinite string.
There are 4 occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring
Input Format

The first line contains a single string, s.
The second line contains an integer, n.

Constraints
1 <= |s| <= 100
1 <= n <= 10^12
for 25% of the test cases, n <= 10^6
'''

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    a_uri = s.count("a")

    inmultire = n // len(s)
    total_litere = len(s) * inmultire
    litere_lipsa = n - total_litere

    rez = a_uri * inmultire + s[0:litere_lipsa].count("a")

    return rez


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
