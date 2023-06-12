import sys

input = sys.stdin.readline
N = int(input().strip())
nums = [0, 0] + [1] * (N - 1)


def sosu(N):
    result = []
    for i in range(2, N + 1):
        k = i * 2
        while k <= N:
            if nums[k] == 1:
                nums[k] = 0
            k = k + i

    for i, num in enumerate(nums):
        if num == 1:
            result.append(i)
    return result


def matching(N, sosu):
    l = len(sosu)
    if l == 0:
        return 0
    st, en, sums, result = 0, 0, 0, 0
    while en < l:
        if sums < N:
            sums += sosu[en]
            en += 1
        elif sums > N:
            sums -= sosu[st]
            st += 1
        else:
            sums += sosu[en]
            result += 1
            en += 1
    if N == sosu[-1]:
        result += 1
    return result


sosus = sosu(N)
answer = matching(N, sosus)
print(answer)
