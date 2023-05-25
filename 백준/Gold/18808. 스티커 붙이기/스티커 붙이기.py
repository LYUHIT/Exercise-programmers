import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
notebook = [[0] * m for _ in range(n)]
stickers = []
answer = 0

for i in range(k):
    y, x = map(int, input().split())
    sticker = []
    for _ in range(y):
        sticker.append(list(map(int, input().split())))
    stickers.append(sticker)


def rotate(now):
    y, x = len(now), len(now[0])
    rotate = []
    for i in range(x):
        temp = []
        for j in range(y - 1, -1, -1):
            temp.append(now[j][i])
        rotate.append(temp)
    return rotate


def putOnNotebookByShift(now):
    y, x = len(now), len(now[0])
    if y > n or x > m:
        return False
    for j in range(n - y + 1):
        for i in range(m - x + 1):

            def checkAndPost():
                for b in range(y):
                    for a in range(x):
                        if notebook[j + b][i + a] * now[b][a] == 1:
                            return False
                else:
                    for b in range(y):
                        for a in range(x):
                            if now[b][a] == 1:
                                notebook[j + b][i + a] = 1
                    return True

            if checkAndPost():
                return True
            else:
                continue
    else:
        False


while stickers:
    now = stickers.pop(0)
    for r in range(4):
        if putOnNotebookByShift(now):
            break
        else:
            now = rotate(now)
            continue
    else:
        continue

for j in range(n):
    for i in range(m):
        if notebook[j][i]:
            answer += 1

print(answer)