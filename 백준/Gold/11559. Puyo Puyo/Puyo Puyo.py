import sys
from collections import deque

input = sys.stdin.readline

imaps = [list(input().strip()) for _ in range(12)]
maps = [["."] * 12 for _ in range(6)]
for j in range(12):
    for i in range(6):
        maps[i][11 - j] = imaps[j][i]

cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
tempdel = deque()
todel = deque()
domore = True
while domore:
    domore = False
    visited = [[0] * 12 for _ in range(6)]
    # 한칸씩 돌면서 주변블럭 확인
    for j in range(6):
        for i in range(12):
            # 기준점이 방문안한 블럭이라면 큐에 추가하고 시작
            if maps[j][i] != "." and visited[j][i] == 0:
                queue.append([j, i, maps[j][i]])
                visited[j][i] = 1
            # 주변 블럭 모두 찾을 때 까지
            while queue:
                now = queue.popleft()
                tempdel.append(now)
                y = now[0]
                x = now[1]
                puyo = now[2]
                # 기준점 주변에 확인
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if (
                        0 <= ny < 6
                        and 0 <= nx < 12
                        and maps[ny][nx] == puyo
                        and visited[ny][nx] == 0
                    ):
                        queue.append([ny, nx, maps[ny][nx]])
                        visited[ny][nx] = 1
            if len(tempdel) >= 4:
                domore = True
                while tempdel:
                    todel.append(tempdel.pop())
            else:
                tempdel.clear()
    while todel:
        now = todel.popleft()
        y, x = now[0], now[1]
        maps[y][x] = "."
    for j in range(6):
        last = 0
        for i in range(12):
            if maps[j][i] != ".":
                maps[j][last], maps[j][i] = maps[j][i], maps[j][last]
                last += 1

    if domore == True:
        cnt += 1

print(cnt)
