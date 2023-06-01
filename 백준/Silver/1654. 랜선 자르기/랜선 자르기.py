import sys

input = sys.stdin.readline
n, m = map(int, input().split())
nums = [int(input().strip()) for _ in range(n)]

srt = 1
end = sum(nums) // m
result = 0
mid = 0
while srt < end:
    mid = (srt + end + 1) // 2
    result = sum(num // mid for num in nums)
    if result >= m:
        srt = mid
    else:
        end = mid - 1
print(srt)
