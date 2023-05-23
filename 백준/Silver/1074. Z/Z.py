import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())
nums = 0


def square(n, r, c):
    global nums
    half = 2 ** (n - 1)
    if n > 0:
        if r < 2 ** (n - 1):
            if c < 2 ** (n - 1):
                nums += half**2 * 0
                square(n - 1, r, c)
            else:
                nums += half**2 * 1
                square(n - 1, r, c - half)
        if r >= 2 ** (n - 1):
            if c < 2 ** (n - 1):
                nums += half**2 * 2
                square(n - 1, r - half, c)

            else:
                nums += half**2 * 3
                square(n - 1, r - half, c - half)

    return nums


print(square(N, r, c))
