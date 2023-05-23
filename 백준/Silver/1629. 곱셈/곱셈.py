import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())


def loop(a, b, c):
    if b == 1:
        return a % c
    rest = loop(a, b // 2, c)
    rest = rest**2 % c
    if b % 2:
        return rest * a % c
    else:
        return rest


print(loop(A, B, C))
