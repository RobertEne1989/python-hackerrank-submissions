'''
Task
Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
m = set(map(int, input().split()))
#m = sorted(m)

b = int(input())
n = set(map(int, input().split()))

res = m.difference(n).union(n.difference(m))
for el in sorted(res):
    print(el)
#print(m.difference(sorted(n)))
#print(n.difference(sorted(m)))
