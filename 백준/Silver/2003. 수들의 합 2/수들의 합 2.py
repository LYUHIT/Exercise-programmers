import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dp = [0]


for i in range(N):
    dp.append(arr[i] + dp[i])

st, en = 0, 0

while st <= en <= N:
    if dp[en] - dp[st] < M:
        en += 1
    else:
        if dp[en] - dp[st] == M:
            answer += 1
        st += 1

print(answer)
