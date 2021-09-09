'''
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0.
For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints
1 <= n <= 10 ^ 5
1 <= m <= 10 ^ 5
1 <= Any integer in the input <= 10 ^ 9

Input Format

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format

Output a single integer, your total happiness.
'''


_ = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
like1 = 0
dislike1 = 0
for elem in array:
    if elem in like:
        like1 += 1
for elem2 in array:
    if elem2 in dislike:
        dislike1 += 1

res = like1 - dislike1
print(res)
