import sys

input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int, input().split()))
m = int(input().strip())
test = list(map(int, input().split()))
answer = []
cartDict = dict()

for card in cards:
    if cartDict.get(card):
        cartDict[card] += 1
    else:
        cartDict[card] = 1

for t in test:
    if cartDict.get(t):
        answer.append(str(cartDict[t]))
    else:
        answer.append("0")

print(" ".join(answer))
