'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5 + 9 = 17.
Their absolute difference is |15 - 17| = 2.

Function description

Complete the diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers

Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer,n, the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row,arr[i], and consists of n space-separated integers arr[i][j].

Constraints
-100 <= arr[i][j] <= 100

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer
'''

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0

    for i in range(len(arr)):
        sum1 += arr[i][i]
        sum2 += arr[i][len(arr) - 1 - i]

    return abs(sum1 - sum2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
