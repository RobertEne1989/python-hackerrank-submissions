'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to
uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string

Input Format

A single line containing a string s.

Constraints
0 < len(s) <= 1000
'''


def swap_case(s):
    res = ""
    for letter in s:
        if letter == letter.lower():
            res += letter.upper()
        else:
            res += letter.lower()
    return res
