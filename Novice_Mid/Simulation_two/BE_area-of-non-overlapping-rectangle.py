OFFSET = 1000
MAX_R = 2000

arr = [ tuple(map( int, input().split())) for _ in range(3)]
box = [ [0]*(MAX_R+1) for _ in range(MAX_R + 1)]

for p_num, (x1, y1, x2, y2) in enumerate(arr, start=1):
    x1 += OFFSET
    y1 += OFFSET
    x2 += OFFSET
    y2 += OFFSET
    for i in range(x1,x2):
        for j in range(y1,y2):
            box[i][j] = 1 if p_num != 3 else 0

area = 0
for i in range(0, MAX_R+1):
    for j in range(0, MAX_R+1):
        if box[i][j]:
            area +=1
            
print(area)