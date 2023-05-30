import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
m = int(input().strip())
b = list(map(int, input().split()))

a.sort()

def find(s, e, f):
    m = (e + s) // 2
    if s == e:         return 0
    if a[m] == f:      return 1
    elif a[m] < f:     return find(m + 1, e, f)
    else:              return find(s, m, f)

for j in b:
    print(find(0, len(a), j))