import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())

maps = []
for _ in range(N):
    maps.append(list(input().strip()))

normal = [[0] * N for _ in range(N)]
blind = [[0] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def f(RG, visited):
    queue = deque()
    answer = 0

    if RG == True:
        color = {"R": ["R", "G"], "G": ["R", "G"], "B": ["B"]}
    else:
        color = {"R": ["R"], "G": ["G"], "B": ["B"]}

    for j in range(N):
        for i in range(N):
            if visited[j][i] == 0:
                c = color[maps[j][i]]
                queue.append([j, i])
                visited[j][i] = 1

                while queue:
                    now = queue.popleft()
                    y = now[0]
                    x = now[1]
                    for r in range(4):
                        ny = y + dy[r]
                        nx = x + dx[r]
                        if (
                            0 <= ny < N
                            and 0 <= nx < N
                            and maps[ny][nx] in c
                            and visited[ny][nx] == 0
                        ):
                            queue.append([ny, nx])
                            visited[ny][nx] = 1
                answer += 1
    return answer


print(f(False, normal))
print(f(True, blind))
