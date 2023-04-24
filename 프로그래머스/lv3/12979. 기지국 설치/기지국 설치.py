import math

def solution(n, stations, w):
    answer = 0
    possible = []
    
    # 통신 가능한 범위 정리
    for station in stations :
        if len(possible) != 0 and station-w <= possible[-1][1]:
            possible[-1][1] = station+w
        else :
            possible.append([station-w,station+w])
    
    def countBase(i):
        share = i//(w*2+1)
        remain = i%(w*2+1)
        if remain > 0 :
            return share+1
        else:
            return share
    
    # 시작점 ~ 첫 통신범위 탐색
    if possible[0][0] > 1:
        impossible = possible[0][0]-1
        answer += countBase(impossible)
    
    # 첫 통신범위 ~ 끝까지 필요한 기지국 수 탐색     
    for i in range(len(possible)):
        if i == len(possible)-1:
            impossible = n-possible[-1][1]
        else:
            impossible = possible[i+1][0]-possible[i][1]-1
        answer += countBase(impossible)
        
    return answer