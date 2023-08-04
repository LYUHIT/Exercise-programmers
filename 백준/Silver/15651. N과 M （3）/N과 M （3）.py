N, M = map(int, input().split())

def combi(arr, cnt):
    for i in range(N):
        arr.append(str(i + 1))
        if cnt == M:
            print(" ".join(arr))
        else:
            combi(arr, cnt + 1)
        arr.pop()

combi([], 1)
