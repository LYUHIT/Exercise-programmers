import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, list(input().strip()))) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append([0, 0, 1])
# visited = [[0] * m for _ in range(n)]
visited = 0


def bfs():
    global visited
    while queue:
        now = queue.popleft()
        y, x, used = now[0], now[1], now[2]
        if x == m - 1 and y == n - 1:
            return used
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (
                    0 <= nx < m
                    and 0 <= ny < n
                    and maps[ny][nx]
                    and not visited & 1 << ny * m + nx
                ):
                    visited |= 1 << ny * m + nx
                    queue.append([ny, nx, used + 1])


print(bfs())