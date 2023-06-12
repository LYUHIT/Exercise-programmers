N = int(input().strip())
times = sorted(list(map(int, input().split())))
answer = 0

for i, time in enumerate(times):
    answer += time * (N - i)

print(answer)
