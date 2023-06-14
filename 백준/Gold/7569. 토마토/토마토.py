import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
answer = 0
queue = deque()

maps = [[list(input().split()) for _ in range(N)] for _ in range(H)]
tomatos = []
for k in range(H):
    for j in range(N):
        for i in range(M):
            if maps[k][j][i] == "1":
                tomatos.append([k, j, i, 0])

for tomato in tomatos:
    queue.append(tomato)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while queue:
    now = queue.popleft()
    z = now[0]
    y = now[1]
    x = now[2]
    cnt = now[3]

    for d in range(6):
        nz = z + dz[d]
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if maps[nz][ny][nx] == "0":
                maps[nz][ny][nx] = "1"
                queue.append([nz, ny, nx, cnt + 1])

    answer = cnt

for k in range(H):
    for j in range(N):
        for i in range(M):
            if maps[k][j][i] == "0":
                answer = -1

print(answer)
