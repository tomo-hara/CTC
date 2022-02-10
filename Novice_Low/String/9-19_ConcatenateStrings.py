""" Write a program that outputs the concatenated version of given strings, given an integer n and n strings. """

string = ""
n = int(input())
for _ in range(n):
    string += "".join(input())

print(string)