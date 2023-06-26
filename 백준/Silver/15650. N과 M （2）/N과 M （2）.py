import sys

input = sys.stdin.readline
N, M = map(int, input().split())

stack = []


def nm():
    if len(stack) != 0:
        for i in range(stack[-1] + 1, N + 1):
            stack.append(i)
            if len(stack) == M:
                print(*stack)
            else:
                nm()
            stack.pop()
    else:
        for i in range(1, N + 1):
            stack.append(i)
            if len(stack) == M:
                print(*stack)
            else:
                nm()
            stack.pop()


nm()
