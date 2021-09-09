'''
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints
0 < N <= 100

Output Format

Print the space separated elements of deque d.
'''


from collections import deque

d = deque()
for i in range(int(input())):
    c = input().split()
    if c[0] == "append":
        d.append(c[1])
    elif c[0] == "appendleft":
        d.appendleft(c[1])
    elif c[0] == "pop":
        d.pop()
    elif c[0] == "popleft":
        d.popleft()
print(*d)
