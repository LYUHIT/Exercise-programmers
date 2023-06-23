import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
rooms = [[*map(int, input().split())] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def lookAround(y, x, d):
    clean(y, x)
    for r in range(3, -1, -1):
        nd = (d + r) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        if 0 <= ny < N and 0 <= nx < M and rooms[ny][nx] == 0:
            return forward(ny, nx, nd)
    else:
        nd = (d + 2) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        back(ny, nx, d)


def forward(y, x, d):
    return lookAround(y, x, d)


def back(y, x, d):
    if rooms[y][x] != 1:
        lookAround(y, x, d)


def clean(y, x):
    global totalClean
    if rooms[y][x] == 0:
        rooms[y][x] = 2
        totalClean += 1


totalClean = 0
lookAround(y, x, d)
print(totalClean)