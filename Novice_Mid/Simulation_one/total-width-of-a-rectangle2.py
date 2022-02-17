# src : https://www.codetree.ai/missions/5/concepts/44/problems/total-width-of-a-rectangle2
# 시뮬레이션 1 - 사각형의 총 넓이 2

n = int(input())
m = n
# x1, x2, y1, y2 = tuple(map(int, input().split()))
OFFSET = 100
MAX_VAL = 201
flood = [
    [0] * MAX_VAL
    for _ in range(MAX_VAL) # 0 to (MAX_VAL - 1)
]
given_inputs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

rectangles = [
    rectangle
    for rectangle in given_inputs
]

for rectangle in rectangles:
    x1, y1, x2, y2 = rectangle
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET \
                    , x2 + OFFSET, y2 + OFFSET
    for i in range(x1, x2): # x1 to (x2 - 1)
        for j in range(y1, y2): # y1 to (y2 - 1)
            flood[i][j] = 1

fill_cnt = 0
for i in range(MAX_VAL): # 0 to (MAX_VAL - 1)
        for j in range(MAX_VAL): # 0 to (MAX_VAL - 1)
            if flood[i][j] == 1:
                fill_cnt += 1
print(fill_cnt)