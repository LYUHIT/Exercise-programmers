def solution(elements):
    answer = 0
    length = len(elements)
    sums =[]
    for e in elements:
        sums.append(e)
    
    for n in range(length+1): #현재 칸수
        if n == 0 or n == 1:
            continue
        for i in range(length): # 이번 칸수 5개 채우기
            m = (i+n-1)%length
            sums.append(sums[(n-2)*length+i] + sums[m])

    answer = len(list(set(sums)))
        
    return answer