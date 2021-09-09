'''
TASK
You are given a set A and N number of other sets. These N number of sets have to perform some specific
mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A.

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2 * N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the
other set.
The second line of each part contains space separated list of elements in the other set.

0 < len(set(A)) < 1000
0 < len(otherSets) < 100
0 < N < 100

Output Format

Output the sum of elements in set A.
'''

nr = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command, _ = input().split()
    s2 = set(map(int, input().split()))
    if command == "intersection_update":
        s1.intersection_update(s2)
    elif command == "update":
        s1.update(s2)
    elif command == "symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    elif command == "difference_update":
        s1.difference_update(s2)

print(sum(s1))
