import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []
distances = []
chickenRoots = []

# 집과 치킨집 파악
for j in range(N):
    for i in range(N):
        if maps[j][i] == 1:
            homes.append([j, i])
        if maps[j][i] == 2:
            chickens.append([j, i])

combi = list(itertools.combinations(chickens, M))

for com in combi:
    totalDistance = 0
    for home in homes:
        distance = N * 2
        for c in com:
            distance = min(distance, abs(home[0] - c[0]) + abs(home[1] - c[1]))
        totalDistance += distance

    distances.append(totalDistance)

print(min(distances))
