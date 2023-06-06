import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = sorted([int(input().strip()) for _ in range(N)])
l = len(A)

st, en = 0, 0
ans = float("inf")

while en < l:
    if M == 0:
        ans = 0
        break

    if A[en] - A[st] >= M:
        ans = min(ans, A[en] - A[st])
        st += 1
    else:
        en += 1

print(ans)
