import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
m = int(input().strip())
b = list(map(int, input().split()))

a.sort()
l = len(a)

def find(s, e, f):
    m = (e + s) // 2

    if s == e:
        if l <= m:
            return 0
        elif a[m] == f:
            return 1
        else:
            return 0
    else:
        if a[m] == f:
            return 1
        else:
            if a[m] < f:
                return find(m + 1, e, f)
            else:
                return find(s, m, f)


for j in b:
    print(find(0, l, j))
