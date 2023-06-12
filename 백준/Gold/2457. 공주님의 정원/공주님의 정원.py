import sys

input = sys.stdin.readline

N = int(input().strip())
flowers = [list(map(int, input().split())) for _ in range(N)]
flowers.sort(key=lambda x: (x[0], x[1], x[2], x[3]))


def next(start, before):
    before_month = before[0]
    before_day = before[1]
    endMonth = 0
    endDay = 0
    NextFlowerIndex = -1
    for i in range(start + 1, len(flowers)):
        flower = flowers[i]
        if flower[0] < before_month or (
            flower[0] == before_month and flower[1] <= before_day
        ):
            if (
                endMonth < flower[2] or (endMonth == flower[2] and endDay <= flower[3])
            ) and (
                flower[2] > before_month
                or (flower[2] == before_month and flower[3] > before_day)
            ):
                endMonth, endDay = flower[2], flower[3]
                NextFlowerIndex = i
    return [NextFlowerIndex, [endMonth, endDay]]


def main():
    nowdate = [3, 1]
    nextflower = -1
    answer = 0

    while nowdate[0] < 12:
        now = next(nextflower, nowdate)
        if now[0] == -1:
            print(0)
            return
        else:
            nextflower = now[0]
            nowdate = now[1]
            answer += 1

    print(answer)


main()
