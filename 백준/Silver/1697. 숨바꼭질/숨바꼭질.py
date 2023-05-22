import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * 100001
queue = deque()
queue.append([n, 0])
answer = 0

while queue:
    now = queue.popleft()
    num, time = now[0], now[1]
    visited[num] = 1
    if num == k:
        answer = time
        break
    if 0 <= num - 1 <= 100000 and not visited[num - 1]:
        queue.append([num - 1, time + 1])
    if 0 <= num + 1 <= 100000 and not visited[num + 1]:
        queue.append([num + 1, time + 1])
    if 0 <= num * 2 <= 100000 and not visited[num * 2]:
        queue.append([num * 2, time + 1])

print(answer)
