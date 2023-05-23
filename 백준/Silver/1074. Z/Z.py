import sys

input = sys.stdin.readline
N, r, c = map(int, input().split())
nums = 0


def square(n, r, c):
    global nums
    if n > 0:
        if r < 2 ** (n - 1):
            if c < 2 ** (n - 1):
                nums += (2 ** (n - 1)) ** 2 * 0
                square(n - 1, r, c)
            else:
                nums += (2 ** (n - 1)) ** 2 * 1
                square(n - 1, r, c - (2 ** (n - 1)))

        if r >= 2 ** (n - 1):
            if c < 2 ** (n - 1):
                nums += (2 ** (n - 1)) ** 2 * 2
                square(n - 1, r - (2 ** (n - 1)), c)

            else:
                nums += (2 ** (n - 1)) ** 2 * 3
                square(n - 1, r - (2 ** (n - 1)), c - (2 ** (n - 1)))

    return nums


print(square(N, r, c))
