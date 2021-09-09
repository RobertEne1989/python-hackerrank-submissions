'''
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code

>>> from collections import Counter
>>>
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>>
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>>
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]

Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of
their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and Xi, the price of
the shoe.

Constraints
0 < X < 10 ^ 3
0 < N  <= 10 ^ 3
20 < Xi < 100
2 < shoe size < 20

Output Format

Print the amount of money earned by Raghu.
'''


number_of_shoes = int(input())
shoe_sizes = input().split()
shoe_sizes_dict = {}
for i in range(len(shoe_sizes)):
    shoe_sizes[i] = int(shoe_sizes[i])
for elem in shoe_sizes:
    if elem in shoe_sizes_dict:
        shoe_sizes_dict[elem] += 1
    else:
        shoe_sizes_dict[elem] = 1

number_of_customers = int(input())
perechi = []
for _ in range(number_of_customers):
    shoe_size, price = input().split()
    shoe_size = int(shoe_size)
    price = int(price)
    perechi.append((shoe_size, price))

suma = 0
for item in perechi:
    if item[0] in shoe_sizes_dict and shoe_sizes_dict[item[0]] != 0:
        shoe_sizes_dict[item[0]] -= 1
        suma += item[1]

print(suma)
