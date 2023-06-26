import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

K = int(input().strip())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input().strip())
actions = deque([list(input().split()) for _ in range(L)])

for action in actions:
    action[0] = int(action[0])


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


lastTime = 0
lastDir = 1
live = True
time = 0
snake = deque()
snake.append([1, 1])


def move(lastDir):
    y, x = snake[0][0], snake[0][1]
    ny = y + dy[lastDir]
    nx = x + dx[lastDir]
    if 0 < ny <= N and 0 < nx <= N and [ny, nx] not in snake:
        snake.appendleft([ny, nx])
        last = snake.pop()
        if [ny, nx] in apples:
            eat([ny, nx])
            grow(last)
    else:
        dead()


def turn(direction):
    global lastDir
    if direction == "L":
        lastDir = (lastDir + 3) % 4
    elif direction == "D":
        lastDir = (lastDir + 1) % 4


def eat(apple):
    apples.remove(apple)


def grow(last):
    snake.append(last)


def dead():
    global live
    live = False


while live:
    time += 1
    move(lastDir)
    if len(actions) != 0 and time == actions[0][0]:
        now = actions.popleft()
        turn(now[1])

print(time)
