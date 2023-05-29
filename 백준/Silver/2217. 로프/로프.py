import sys

input = sys.stdin.readline
n = int(input().strip())
lopes = [int(input().strip()) for _ in range(n)]

slopes = sorted(lopes, reverse=True)
count = 0
maximum = 0

for sl in slopes:
    count += 1
    now = sl * count
    if maximum <= now:
        maximum = now

print(maximum)