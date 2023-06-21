import sys

input = sys.stdin.readline
n, m, y, x, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))
dice = [0] * 6


def up():
    dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]


def down():
    dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]


def left():
    dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]


def right():
    dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]


for order in orders:
    if order == 1:
        if x == m - 1:
            continue
        right()
        x += 1
    elif order == 2:
        if x == 0:
            continue
        left()
        x -= 1
    elif order == 3:
        if y == 0:
            continue
        up()
        y -= 1
    elif order == 4:
        if y == n - 1:
            continue
        down()
        y += 1

    if maps[y][x] == 0:
        maps[y][x] = dice[5]
    else:
        dice[5] = maps[y][x]
        maps[y][x] = 0

    print(dice[0])
