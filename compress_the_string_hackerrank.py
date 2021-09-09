'''
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

Constraints
All the characters of S denote integers between 0 and 9.

1 <= |S| <= 10 ^ 4

Sample Input
1222311

Sample Output
(1, 1) (3, 2) (1, 3) (2, 1)

Explanation

First, the character 1 occurs only once. It is replaced by (1, 1). Then the 2 character  occurs three times,
and it is replaced by (3, 2)  and so on.

Also, note the single space within each compression and between the compressions.
'''

s = input()
l = [int(s[0]), 1]

for i in range(1, len(s)):
    if int(s[i]) == l[0]:
        l[1] += 1
    else:
        print("(", l[1], ", ", l[0], ")", sep="", end=' ')
        l[0] = int(s[i])
        l[1] = 1
print("(", l[1], ", ", l[0], ")", sep="", end=' ')
