import sys

input = sys.stdin.readline
n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]

nums = sorted(nums)
l1 = len(nums) - 1

sums2 = []
for i in range(l1):
    for j in range(i + 1):
        sums2.append(nums[i] + nums[j])

sums2 = list(sorted(set(sums2)))  # 정렬 해 말아?
l2 = len(sums2) - 1


def find(s, e, f):
    if f < sums2[s] or sums2[e] < f:
        return 0
    m = (s + e) // 2

    if sums2[m] == f:
        return f
    elif sums2[m] < f:
        return find(m + 1, e, f)
    elif f < sums2[m]:
        return find(s, m, f)


def matching():
    for sum3 in range(l1, -1, -1):
        for num1 in range(sum3, -1, -1):
            now = nums[sum3] - nums[num1]
            if find(0, l2, now):
                return nums[sum3]


print(matching())
