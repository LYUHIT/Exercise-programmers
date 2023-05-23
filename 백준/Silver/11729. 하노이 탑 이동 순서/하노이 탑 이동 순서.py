import sys

input = sys.stdin.readline
n = int(input().strip())
count = 0
moving = []


def move(n, s, e):
    global count
    if n > 1:
        if s == 1:
            if e == 2:
                t = 3
            elif e == 3:
                t = 2
        if s == 2:
            if e == 1:
                t = 3
            elif e == 3:
                t = 1
        if s == 3:
            if e == 1:
                t = 2
            elif e == 2:
                t = 1
        move(n - 1, s, t)
        move(1, s, e)
        move(n - 1, t, e)
    else:
        count += 1
        moving.append([s, e])


move(n, 1, 3)
print(count)
for m in moving:
    print(m[0], m[1])
