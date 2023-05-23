import sys

input = sys.stdin.readline
n = int(input().strip())
count = 0
moving = []


def move(n, s, e):
    global count
    if n > 1:
        t = 6 - (s + e)
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
