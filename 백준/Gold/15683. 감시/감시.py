import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(n)]
map2 = [[0] * m for _ in range(n)]
answer = 0

for j in range(n):
    for i in range(m):
        if maps[j][i] == 6:
            map2[j][i] = "#"
        else:
            map2[j][i] = 0
            answer += 1


cctvs = []

# CCTV 위치 파악
for j in range(n):
    for i in range(m):
        if maps[j][i] != 0 and maps[j][i] != 6:
            cctvs.append([j, i])


# cctv 방향에 맞춰 켜기
def turn(onOff, cctv, direct):
    if onOff == "on":
        o = 1
    elif onOff == "off":
        o = -1
    y, x = cctv[0], cctv[1]

    while direct > 3:
        direct -= 4

    def looking(d, start, end):
        if d == 0:
            for j in range(start, end, -1):
                if maps[j][x] == 6:
                    break
                else:
                    map2[j][x] += o
        if d == 1:
            for i in range(start, end):
                if maps[y][i] == 6:
                    break
                else:
                    map2[y][i] += o
        if d == 2:
            for j in range(start, end):
                if maps[j][x] == 6:
                    break
                else:
                    map2[j][x] += o
        if d == 3:
            for i in range(start, end, -1):
                if maps[y][i] == 6:
                    break
                else:
                    map2[y][i] += o

    if direct == 0:
        looking(0, y, -1)
    elif direct == 1:
        looking(1, x, m)
    elif direct == 2:
        looking(2, y, n)
    elif direct == 3:
        looking(3, x, -1)


def cctv(a):
    global answer
    if a == len(cctvs):
        count = 0
        for j in range(n):
            for i in range(m):
                if map2[j][i] == 0:
                    count += 1
        if answer > count:
            answer = count
    else:
        now = cctvs[a]
        y, x = now[0], now[1]
        t = maps[y][x]

        if t == 1:
            for d in range(4):
                turn("on", now, d)
                cctv(a + 1)
                turn("off", now, d)
        if t == 2:
            for d in range(2):
                turn("on", now, d)
                turn("on", now, d + 2)
                cctv(a + 1)
                turn("off", now, d)
                turn("off", now, d + 2)
        if t == 3:
            for d in range(4):
                turn("on", now, d)
                turn("on", now, d + 1)
                cctv(a + 1)
                turn("off", now, d)
                turn("off", now, d + 1)
        if t == 4:
            for d in range(4):
                turn("on", now, d)
                turn("on", now, d + 1)
                turn("on", now, d + 2)
                cctv(a + 1)
                turn("off", now, d)
                turn("off", now, d + 1)
                turn("off", now, d + 2)
        if t == 5:
            for d in range(4):
                turn("on", now, d)
            cctv(a + 1)
            for d in range(4):
                turn("off", now, d)


cctv(0)

print(answer)
