import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
tofroms = [list(map(int, input().split())) for _ in range(m)]

sums = [0] + nums.copy()
for i in range(2, n + 1):
    sums[i] = sums[i - 1] + sums[i]
for tofrom in tofroms:
    print(sums[tofrom[1]] - sums[tofrom[0] - 1])