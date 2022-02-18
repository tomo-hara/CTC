# src : https://www.codetree.ai/missions/5/concepts/44/problems/area-of-non-overlapping-rectangle
# 시뮬레이션1 - 겹치지 않는 사각형의 넓이
OFFSET = 1000
MAX_RANGE = 2001

"""
1 2 3 5
6 0 10 4
2 1 8 3
"""
flood = [
    [0 for _ in range(MAX_RANGE)]
    for _ in range(MAX_RANGE)
]
rects = [
    tuple(map(int, input().split()))
    for _ in range(3)
]

for i, rect in enumerate(rects, start=1):
    x1, y1, x2, y2 = rect
    x1, y1, x2, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
    for x in range(x1, x2):
        for y in range(y1, y2):
            flood[x][y] = i


cnt = 0
for x in range(MAX_RANGE):
    for y in range(MAX_RANGE):
        if flood[x][y] == 1 or flood[x][y] == 2:
            cnt += 1
print(cnt)