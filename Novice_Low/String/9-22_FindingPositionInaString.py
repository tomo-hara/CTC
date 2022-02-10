""" Write a program that outputs the position of a given alphabet in the given string. The position of first letter of the string is 0. """

string, niddle= input().split()

if niddle in string:
    print(string.index(niddle))
else:
    print("No")