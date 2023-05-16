import sys

input = sys.stdin.readline
n, m = map(int, input().split())
visited = [0] * n
nums = [0] * m
answer = []


def dfs(k):
    if k == m:
        print(" ".join(nums))
    else:
        for i in range(n):
            if visited[i]:
                continue
            else:
                visited[i] = 1
                nums[k] = str(i + 1)
                dfs(k + 1)
                visited[i] = 0


dfs(0)