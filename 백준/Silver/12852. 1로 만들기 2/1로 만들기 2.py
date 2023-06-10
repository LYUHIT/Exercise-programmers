import sys
from collections import deque

input = sys.stdin.readline

X = int(input().strip())

# [카운트, 이전숫자]
m = [[i, 0, 0] for i in range(X + 1)]

queue = deque()
queue.append(1)

while queue:
    now = queue.popleft()
    if now * 3 <= X and m[now * 3][1] == 0:
        m[now * 3][1] = m[now][1] + 1
        m[now * 3][2] = now
        queue.append(now * 3)

    if now * 2 <= X and m[now * 2][1] == 0:
        m[now * 2][1] = m[now][1] + 1
        m[now * 2][2] = now
        queue.append(now * 2)

    if now + 1 <= X and m[now + 1][1] == 0:
        m[now + 1][1] = m[now][1] + 1
        m[now + 1][2] = now
        queue.append(now + 1)

answer = []
now = X

while now > 0:
    answer.append(str(now))
    now = m[now][2]

print(m[X][1])
print(" ".join(answer))
