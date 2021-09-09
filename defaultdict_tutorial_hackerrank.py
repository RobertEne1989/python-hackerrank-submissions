'''
In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
Print the indices of each occurrence of m in group A. If it does not appear, print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A. The second word, 'c', does not
appear in group A, so print -1.

Expected output:

1 3
-1

Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints
1 <= n <= 10000
1 <=m <= 100
1 <= length of each word in the input <= 100

Output Format

Output m lines.
The i-th line should contain the 1-indexed positions of the occurrences of the i-th word separated by spaces.
'''

from collections import defaultdict

n, m = map(int, input().split(" "))
input1 = list()
for i in range(n):
    input1.append(input())

input2 = list()
for i in range(m):
    input2.append(input())

d = defaultdict(list)

for i in range(n):
    d[input1[i]].append(i + 1)

for i in input2:
    if i in d:
        print(*d[i])
    else:
        print(-1)
