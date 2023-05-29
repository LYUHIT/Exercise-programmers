import sys

input = sys.stdin.readline

answer = 0
n, k = map(int, input().split())
coins = [int(input().strip()) for _ in range(n)]
coins.reverse()


for c in coins:
    if c <= k:
        answer += k // c
        k %= c

print(answer)