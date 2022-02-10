string = input().split()

# rev_string = string[::-1]

# for i in range(10):
#     print(rev_string[i])


for elem in string[::-1]:
    print(elem, sep="", end="")