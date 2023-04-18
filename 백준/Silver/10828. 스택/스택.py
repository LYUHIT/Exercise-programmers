import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == 'push':
        stack.append(word[1])
    elif order == 'pop':
        if len(stack):
            poped = stack.pop()
            print(poped)
        else:
            print(-1)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack):
            print (0)
        else:
            print (1)
    elif order == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)