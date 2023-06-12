import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
M = int(input().strip())
tests = list(map(int, input().split()))

answer = ["0"] * M
s_cards = sorted(cards)

for i, test in enumerate(tests):
    st = 0
    en = N - 1

    while st <= en:
        mid = (st + en + 1) // 2
        if test < s_cards[mid]:
            en = mid - 1
        elif s_cards[mid] < test:
            st = mid + 1
        else:
            answer[i] = "1"
            break

print(" ".join(answer))