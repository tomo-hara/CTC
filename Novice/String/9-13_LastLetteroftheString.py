# Output the strings that ends with the given alphabet. If none exists, output 'None'.

string = [
    input()
    for _ in range(10)
]
niddle = input()
flag = False # not exist
for elem in string:
    if elem[-1] == niddle:
        print(elem)
        flag = True
if (flag == False):
    print(None)