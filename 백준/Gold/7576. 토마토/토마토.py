import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [(list(map(int, input().split()))) for _ in range(n)]
queue = deque()
period = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for j in range(n):
    for i in range(m):
        if box[j][i] == 1:
            queue.append([j, i, 0])

while queue:
    now = queue.popleft()
    y, x, day = now[0], now[1], now[2]
    period = day

    for r in range(4):
        if 0 <= y + dy[r] < n and 0 <= x + dx[r] < m and box[y + dy[r]][x + dx[r]] == 0:
            box[y + dy[r]][x + dx[r]] = 1
            queue.append([y + dy[r], x + dx[r], day + 1])

for j in range(n):
    for i in range(m):
        if box[j][i] == 0:
            period = -1
        else:
            continue

print(period)
