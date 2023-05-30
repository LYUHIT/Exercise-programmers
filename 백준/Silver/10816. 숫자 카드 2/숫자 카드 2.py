import sys

input = sys.stdin.readline
n = int(input().strip())
cards = list(map(int, input().split()))
m = int(input().strip())
tests = list(map(int, input().split()))

answer = []
cartDict = dict()

for card in cards:
    cartDict[card] = cartDict.get(card, 0) + 1

for test in tests:
    answer.append(str(cartDict.get(test, 0)))

print(" ".join(answer))
