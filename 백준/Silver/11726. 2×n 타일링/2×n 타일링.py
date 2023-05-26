import sys

input = sys.stdin.readline
n = int(input().strip())

square = [0, 1, 2]
for i in range(3, n + 1):
    square.append(square[-1] + square[-2])
print(square[n] % 10007)
