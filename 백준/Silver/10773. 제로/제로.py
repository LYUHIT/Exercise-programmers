import sys

input = sys.stdin.readline
stack = []
n = int(input().strip())

for _ in range(n):
    now = int(input().strip())
    if now == 0:
        stack.pop()
    else:
        stack.append(now)

print(sum(stack))
