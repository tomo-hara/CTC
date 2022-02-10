""" Write a program that replaces the second letter and the second letter 
from back of the given string with 'a' and outputs the result string. """

# 슬라이싱
s = input()
s = s[:1] + 'a' + s[2:-2] + 'a' + s[-1:]
print(s)

# 리스트
s = list(input())
s[1] = s[-2] = 'a'
string = ""
string = "".join(s)
print(string)