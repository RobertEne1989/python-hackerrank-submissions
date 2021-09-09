'''
Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.

Constraints
0 < N <= 100

Output Format

Print the item_name and net_price in order of its first occurrence.
'''


from collections import OrderedDict

N = int(input())
dct = OrderedDict()
for i in range(N):
    l = input().split()
    name = " ".join(l[:-1])
    price = int(l[-1])
    if name in dct:
        dct[name] += price
    else:
        dct[name] = price
for k, v in dct.items():
    print(k, v)
