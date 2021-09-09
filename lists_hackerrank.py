'''
Consider a list (list = []). You can perform the following commands:

1 insert i e: Insert integer e at position i.
2 print: Print the list.
3 remove e: Delete the first occurrence of integer e.
4 append e: Insert integer e at the end of the list.
5 sort: Sort the list.
6 pop: Pop the last element from the list.
7 reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the
7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer,n , denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

'''


if __name__ == '__main__':
    N = int(input().strip())

    l = []
    for i in range(N):
        args = input().strip().split(" ")
        if args[0] == "append":
            l.append(int(args[1]))
        elif args[0] == "insert":
            l.insert(int(args[1]), int(args[2]))
        elif args[0] == "remove":
            l.remove(int(args[1]))
        elif args[0] == "sort":
            l.sort()
        elif args[0] == "pop":
            l.pop()
        elif args[0] == "reverse":
            l.reverse()
        elif args[0] == "print":
            print(l)
