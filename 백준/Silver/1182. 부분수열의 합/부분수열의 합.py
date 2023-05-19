import sys

input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0


def calc(sums, i):
    global answer
    if i == n - 1:
        if sums + nums[i] == s:
            answer += 1
        if sums == s:
            answer += 1
    else:
        calc(sums + nums[i], i + 1)
        calc(sums, i + 1)


calc(0, 0)
if s == 0:
    answer -= 1
print(answer)
