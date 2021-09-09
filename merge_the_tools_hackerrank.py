'''
Consider the following:

A string,S, of length n where S = c0c1...cN-1
An integer,k, where k is a factor of n.
We can split S into n/k substrings where each subtring,Ti, consists of a contiguous block of k characters in S.
Then, use each Ti to create string Ui such that:

The characters in Ui are a subsequence of the characters in Ti.
Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once.
In other words, if the character at some index j in Ti occurs at a previous index <j in Ti, then do not
include the character in string Ui.
Given S and k, print n/k lines where each line i denotes string Ui.

Example
S = "AAABCADDE"
k=3

There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters,
 so U1='A'. The second substring has all distinct characters, so U2='BCA'. The third substring has 2 different
 characters, so U3='DE'.
  Note that a subsequence maintains the original order of characters encountered. The order of characters
   in each subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

  string s: the string to analyze
  int k: the size of substrings to analyze

Prints
Print each subsequence on a new line. There will be n/k of them. No return value is expected.

Input Format

The first line contains a single string, S.
The second line contains an integer,k, the length of each substring

Constraints

1 <= n <= 10 ^ 4, where n is the length of S
1 <= k <= n
It is guaranteed that n is a multiple of k.
'''


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        l = ""
        for j in string[i:i + k]:
            if j not in l:
                l += j
        print(l)
