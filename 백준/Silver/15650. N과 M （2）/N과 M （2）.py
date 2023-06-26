import sys

input = sys.stdin.readline
N, M = map(int, input().split())

stack = []


def nm(a):
    for i in range(a + 1, N + 1):
        stack.append(i)
        if len(stack) == M:
            print(*stack)
        else:
            nm(i)
        stack.pop()


nm(0)
