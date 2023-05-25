import sys

input = sys.stdin.readline
N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def rotate(board, direction):
    direction %= 4
    newboard = [[0] * 20 for _ in range(N)]
    for j in range(N):
        for i in range(N):
            if direction == 0:
                return board
            if direction == 1:
                newboard[j][i] = board[N - i - 1][j]
            elif direction == 2:
                newboard[j][i] = board[N - j - 1][N - i - 1]
            elif direction == 3:
                newboard[j][i] = board[i][N - j - 1]
    return newboard


def merge(board):
    newboard = [[] for _ in range(N)]
    possible = True
    for j in range(N):
        for i in range(N):
            if board[j][i]:
                if 0 < len(newboard[j]) and newboard[j][-1] == board[j][i] and possible:
                    newboard[j][-1] *= 2
                    possible = False
                else:
                    newboard[j].append(board[j][i])
                    possible = True
        while len(newboard[j]) < N:
            newboard[j].append(0)
    return newboard


def calc(board, d):
    rotatedBoard = rotate(board, d)
    mergedBoard = merge(rotatedBoard)
    finalBoard = rotate(mergedBoard, 4 - d)
    return finalBoard


def findBiggest(board):
    biggest = 0
    for j in range(N):
        for i in range(N):
            if biggest < board[j][i]:
                biggest = board[j][i]
    return biggest


def swipe(board, life):
    global answer
    if life == 0:
        tmpBig = findBiggest(board)
        if answer < tmpBig:
            answer = tmpBig
    else:
        for d in range(4):
            nextboard = calc(board, d)
            swipe(nextboard, life - 1)


swipe(board, 5)
print(answer)