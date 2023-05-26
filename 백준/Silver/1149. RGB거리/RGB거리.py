import sys

input = sys.stdin.readline
N = int(input().strip())
paint = [list(map(int, input().split())) for _ in range(N)]

R = [0] * (N + 1)
G = [0] * (N + 1)
B = [0] * (N + 1)

R[1], G[1], B[1] = paint[0][0], paint[0][1], paint[0][2]

for i in range(2, N + 1):
    R[i] = min(G[i - 1], B[i - 1]) + paint[i - 1][0]
    G[i] = min(R[i - 1], B[i - 1]) + paint[i - 1][1]
    B[i] = min(R[i - 1], G[i - 1]) + paint[i - 1][2]

print(min(R[N], G[N], B[N]))