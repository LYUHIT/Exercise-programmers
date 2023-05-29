import sys

input = sys.stdin.readline
n = int(input().strip())
meeting = [list(map(int, input().split())) for _ in range(n)]
smeeting = sorted(meeting, key=lambda meet: (meet[1], meet[0]))
last = 0
answer = 0

for smeet in smeeting:
    if last <= smeet[0]:
        answer += 1
        last = smeet[1]

print(answer)
