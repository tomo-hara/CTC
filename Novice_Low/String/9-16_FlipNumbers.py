# Output the natural number backwards. However, do not print 0 if it is the first digit of the output.

n = input()
i = 0
while n[::-1][i] == '0':
	i += 1
for j in range(len(n) - i - 1, -1, -1):
	print(n[j], end="")

# for elem in n[::-1]:
#     if elem != '0':
#         print(elem, end="")

num_str = input()

can_print = False

for digit in num_str[::-1]:
    if digit != '0':
        can_print = True
    if can_print:
        print(digit, end="")