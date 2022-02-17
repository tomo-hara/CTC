# src : https://www.codetree.ai/missions/5/concepts/45/problems/move-in-direction
# dx-dy - 방향에 맞춰 이동

x, y = 0, 0
nx, ny = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

mapper = {
    'E' : 0,
    'S' : 1,
    'W' : 2,
    'N' : 3
}
n = int(input())
directions = [
    tuple(input().split())
    for _ in range(n)
]

for direction, dist in directions:
    direct = mapper[direction]
    nx += x + dx[direct] * int(dist)
    ny += y + dy[direct] * int(dist)

print(nx, ny)