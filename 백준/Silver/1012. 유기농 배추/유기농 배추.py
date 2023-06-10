import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0] * M for _ in range(N)]
    queue = deque()
    answer = 0

    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for j in range(N):
        for i in range(M):
            if maps[j][i] == 1:
                queue.append([j, i])
                maps[j][i] = 0

                while queue:
                    now = queue.popleft()

                    y, x = now[0], now[1]
                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if 0 <= ny < N and 0 <= nx < M and maps[ny][nx] == 1:
                            queue.append([ny, nx])
                            maps[ny][nx] = 0
                answer += 1

    print(answer)
