n = int(input())

string = [
    input()
    for _ in range(n)
]

total_len = 0
cnt = 0

for i in range(n):
    total_len += len(string[i])
    if string[i][0] == 'a':
        cnt += 1
    
print(total_len, cnt)