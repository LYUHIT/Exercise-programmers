# 0 < a < b <c < d (a,b는 그룹A, c,d는 그룹B) 일 때,
# ad+bc 보다 작은값은 존재한다 (가정)
# ab + cd < ad + bc 식을 정리하면 c > d
# 모순이므로 가정은 거짓
# 따라서 ad+bc 이 가장 작은 값이다.

import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
a.sort()
b.sort(reverse=True)

for i in range(n):
    answer += a[i] * b[i]
print(answer)
