import sys

input = sys.stdin.readline

text = input().strip()
n = int(input().strip())
turns = [list(input().split()) for _ in range(n)]

dat = [-1, -1]
pre = [-1, 0]
nxt = [1, -1]
cursor = 1


def L(cursor):
    if cursor == nxt[0]:
        return nxt[0]
    else:
        return pre[cursor]


def D(cursor):
    if cursor == 1:
        return 1
    else:
        return nxt[cursor]


def B(cursor):
    if cursor == nxt[0]:
        return nxt[0]
    else:
        pre[cursor] = pre[pre[cursor]]
        nxt[pre[cursor]] = cursor
        return cursor


def P(cursor, char):
    dat.append(char)
    pre.append(pre[cursor])
    nxt.append(cursor)
    nxt[pre[cursor]] = len(dat) - 1
    pre[cursor] = len(dat) - 1
    return cursor


def out():
    answer = []
    cur = nxt[0]
    while cur != 1:
        answer.append(dat[cur])
        cur = D(cur)
    print("".join(answer))


for t in text:
    P(cursor, t)

for t in turns:
    if t[0] == "L":
        cursor = L(cursor)
    elif t[0] == "D":
        cursor = D(cursor)
    elif t[0] == "B":
        cursor = B(cursor)
    elif t[0] == "P":
        cursor = P(cursor, t[1])


out()