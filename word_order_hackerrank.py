'''
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. See the sample
input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1 <= n <= 10 ^ 5

The sum of the lengths of all the words do not exceed 10 ^ 6
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in
the input.


'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list()
for i in range(n):
    l.append(input())

d = dict()
for item in l:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

print(len(d))
for i in d:
    print(d[i], end=" ")
