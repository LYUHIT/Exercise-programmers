import sys

input = sys.stdin.readline
n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]

if n == 1:
    print(stairs[0])

else:
    dp1 = [0] * (n + 1)  # 전칸
    dp2 = [0] * (n + 1)  # 전전칸
    # 초기값 설정
    dp1[1] = stairs[0]
    dp2[1] = stairs[0]

    for i in range(2, n + 1):
        dp1[i] = dp2[i - 1] + stairs[i - 1]
        dp2[i] = max(dp1[i - 2], dp2[i - 2]) + stairs[i - 1]

    print(max(dp1[n], dp2[n]))
