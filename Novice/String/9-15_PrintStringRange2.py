# Write a program that prints n characters from back of the given string backwards, given a string and an integer n.

string = input()
n = int(input())

str_len = len(string)
cnt = 0

for i in range(str_len - 1, -1, -1):
	if cnt >= n:
		break
	print(string[i], end="")
	cnt += 1