import sys

input = sys.stdin.readline
n = int(input().strip())
tri = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n + 1)]

for j in range(n):
    for i in range(j + 1):
        if j == 0 and i == 0:
            dp[j][i] = tri[j][i]
        else:
            if i == 0:
                dp[j][i] = tri[j][i] + dp[j - 1][i]
            elif i == j:
                dp[j][i] = tri[j][i] + dp[j - 1][i - 1]
            else:
                dp[j][i] = max(tri[j][i] + dp[j - 1][i - 1], tri[j][i] + dp[j - 1][i])

answer = max(dp[-1])
print(answer)
