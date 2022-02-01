""" Write a program that outputs 5 letters of the given strings in order in each line, given the number of strings and the strings. """

string = ""
n = int(input())
string += "".join(input().split())

for i in range(len(string)):
    print(string[i], end="")
    if i % 5 == 4:
        print()