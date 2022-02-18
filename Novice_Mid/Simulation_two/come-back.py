# src : https://www.codetree.ai/missions/5/concepts/45/problems/come-back
# 시뮬레이션2 - 되돌아오기
from typing import List

mapper = {
    'E' : 0,
    'W' : 1,
    'S' : 2,
    'N' : 3,
}

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def calc_time(commands : List[tuple], x : int, y : int) -> int:
    nx, ny = x, y
    elapsed_time = 0
    for command in commands:
        direction, dist = command
        direct = mapper[direction]
        for i in range(int(dist)):
            nx, ny = nx + dx[direct], ny + dy[direct]
            elapsed_time += 1
            # print(f'{i} : {direct}, {nx}, {ny}')
            if nx == x and ny == y:
                return elapsed_time

    return -1


n = int(input())
queries = [
    tuple(input().split())
    for _ in range(n)
]

x, y = 0, 0
print(calc_time(queries, x, y))
