import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
maps = [list(input().strip()) for _ in range(m)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
queue = deque()
jtime = 0
jihoon = []

for j in range(m):
    for i in range(n):
        if maps[j][i] == "F":
            queue.append([j, i, 0])
        elif maps[j][i] == "J":
            jihoon = [j, i]

queue.appendleft([jihoon[0], jihoon[1], 0])


def bfs():
    global jtime
    while queue:
        now = queue.popleft()
        y, x, time = now[0], now[1], now[2]

        if maps[y][x] == "J":
            if y == 0 or y == m - 1 or x == 0 or x == n - 1:
                return time + 1
            else:
                for r in range(4):
                    ny, nx = y + dy[r], x + dx[r]
                    if 0 <= ny < m and 0 <= nx < n:
                        if maps[ny][nx] == ".":
                            maps[ny][nx] = "J"
                            queue.append([ny, nx, time + 1])
                maps[y][x] = ","
                jtime = time + 1

        elif maps[y][x] == "F":
            if time > jtime:
                return "IMPOSSIBLE"
            for r in range(4):
                ny, nx = y + dy[r], x + dx[r]
                if 0 <= ny < m and 0 <= nx < n:
                    if maps[ny][nx] == "." or maps[ny][nx] == ",":
                        maps[ny][nx] = "F"
                        queue.append([ny, nx, time + 1])
                    elif maps[ny][nx] == "J":
                        maps[ny][nx] = "F"
    return "IMPOSSIBLE"


print(bfs())
