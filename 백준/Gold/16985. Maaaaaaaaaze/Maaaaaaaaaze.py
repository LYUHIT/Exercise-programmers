import sys
import itertools
from collections import deque

input = sys.stdin.readline
pans = []
for _ in range(5):
    pans.append([list(map(int, input().split())) for _ in range(5)])


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
possible = []


def rotate(pan, angle):
    newpan = [[0] * 5 for _ in range(5)]
    if angle == 0:
        return pan

    elif angle == 1:
        for j in range(5):
            for i in range(5):
                newpan[i][4 - j] = pan[j][i]
        return newpan

    elif angle == 2:
        for j in range(5):
            for i in range(5):
                newpan[4 - j][4 - i] = pan[j][i]
        return newpan

    elif angle == 3:
        for j in range(5):
            for i in range(5):
                newpan[4 - i][j] = pan[j][i]
        return newpan


def mazing(p1, p2, p3, p4, p5):
    mazes = list(itertools.permutations([p1, p2, p3, p4, p5], 5))
    mazeSet = []
    for maze in mazes:
        if maze in mazeSet:
            continue
        else:
            mazeSet.append(maze)
    return mazeSet


def escape(maze, start):
    queue = deque()
    queue.append([0, start[0], start[1], 0])
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    while queue:
        now = queue.popleft()
        z, y, x = now[0], now[1], now[2]
        cnt = now[3]
        if z == 4 and y == (4 - start[0]) and x == (4 - start[1]):
            return cnt
        for d in range(6):
            nx = x + dx[d]
            ny = y + dy[d]
            nz = z + dz[d]
            if (
                0 <= nx < 5
                and 0 <= ny < 5
                and 0 <= nz < 5
                and maze[nz][ny][nx] == 1
                and visited[nz][ny][nx] != 1
            ):
                visited[nz][ny][nx] = 1
                queue.append([nz, ny, nx, cnt + 1])
    return float("inf")


for r1 in range(4):
    for r2 in range(4):
        for r3 in range(4):
            for r4 in range(4):
                for r5 in range(4):
                    p1 = rotate(pans[0], r1)
                    p2 = rotate(pans[1], r2)
                    p3 = rotate(pans[2], r3)
                    p4 = rotate(pans[3], r4)
                    p5 = rotate(pans[4], r5)
                    for maze in mazing(p1, p2, p3, p4, p5):
                        if maze[0][0][0] == 1 and maze[4][4][4] == 1:
                            possible.append(escape(maze, [0, 0]))
                        if maze[0][0][4] == 1 and maze[4][4][0] == 1:
                            possible.append(escape(maze, [0, 4]))
                        if maze[0][4][0] == 1 and maze[4][0][4] == 1:
                            possible.append(escape(maze, [4, 0]))
                        if maze[0][4][4] == 1 and maze[4][0][0] == 1:
                            possible.append(escape(maze, [4, 4]))
if len(possible) > 0:
    minValue = min(possible)
    if minValue > 125:
        answer = -1
    else:
        answer = minValue
else:
    answer = -1
print(answer)
