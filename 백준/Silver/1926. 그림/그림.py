import sys

n, m = map(int, sys.stdin.readline().split())

maps = []
queue = []
sizes = []

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

for _ in range(n):
    word = list(map(int,sys.stdin.readline().split()))
    maps.append(word)

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            queue.append([i, j])
            size = 0
            maps[i][j] = 0
            while queue:
                now = queue.pop(0)
                size += 1
                for a in range(len(x)):
                    nx = now[0] + x[a]
                    ny = now[1] + y[a]
                    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                        queue.append([nx, ny])
                        maps[nx][ny] = 0
            sizes.append(size)

if sizes:
    print("{}\n{}".format(len(sizes), max(sizes)))
else:
    print("0\n0")
