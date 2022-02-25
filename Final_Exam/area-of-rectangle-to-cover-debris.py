# src : https://www.codetree.ai/problems/minimum-area-of-rectangle-to-cover-debris
# 기말고사 - 잔해물을 덮기 위한 사각형의 최소 넓이

import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
OFFSET = 1000
MAX_R = 2000

grid = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

x1, y1, x2, y2 = tuple(map(int, input().split()))
x1, y1, x2, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
for x in range(x1, x2):
    for y in range(y1, y2):
        grid[x][y] += 1


x1, y1, x2, y2 = tuple(map(int, input().split()))
x1, y1, x2, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
for x in range(x1, x2):
    for y in range(y1, y2):
        grid[x][y] *= 0

min_x, min_y = INT_MAX, INT_MAX
max_x, max_y = INT_MIN, INT_MIN
first_rect_exist = False
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if grid[x][y] == 1:
            first_rect_exist = True
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
if not first_rect_exist:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)
print(area)