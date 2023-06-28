import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0
max_pos = max(map(max, board))


def dfs(y, x, s, n):
    global answer
    if answer >= s + max_pos * (4 - n):
        return
    if n == 4:
        answer = max(answer, s)
        return
    else:
        for r in range(4):
            ny, nx = y + dy[r], x + dx[r]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                if n == 2:
                    visited[ny][nx] = 1
                    dfs(y, x, s + board[ny][nx], n + 1)
                    visited[ny][nx] = 0
                visited[ny][nx] = 1
                dfs(ny, nx, s + board[ny][nx], n + 1)
                visited[ny][nx] = 0


for j in range(N):
    for i in range(M):
        visited[j][i] = 1
        dfs(j, i, board[j][i], 1)
        visited[j][i] = 0


print(answer)
