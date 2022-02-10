string = input().split()
total_len = 0

for elem in string:
	length = len(elem)
	total_len += length

print(total_len)