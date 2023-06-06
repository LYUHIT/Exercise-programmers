import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = []
for i, num in enumerate(nums):
    if i == 0:
        dp.append(num)
    else:
        dp.append(dp[-1] + num)

st, en = 0, 0
ans = N + 1
while st <= en < N:
    if dp[en] - dp[st] + nums[st] < M:
        en += 1
    else:
        ans = min(ans, en - st + 1)
        st += 1

if ans == N + 1:
    ans = 0

print(ans)
