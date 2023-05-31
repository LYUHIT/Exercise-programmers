import sys

input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int, input().split()))

answer = []
snums = {value: index for index, value in enumerate(sorted(list(set(nums))))}

for num in nums:
    answer.append(str(snums[num]))

print(" ".join(answer))