import sys

input = sys.stdin.readline
n, m = map(int, input().split())
answer = []

def dfs(num, visited):
    if len(num) == m:
        result = " ".join(num)
        answer.append(result)
    else:
        for i in range(n):
            tnum = num.copy()
            tvisited = visited
            if visited & (1 << i):
                continue
            else:
                tvisited |= 1 << i
                tnum.append(str(i + 1))
                dfs(tnum, tvisited)
    return

dfs([], 0)

print("\n".join(answer))
