def solution(elements):
    answer = 0
    length = len(elements)
    sums =[]
    
    # 초기값 설정
    sums.extend(elements)
    
    # 3칸짜리의 합은 2칸짜리 + 1칸짜리
    # 4칸짜리의 합은 3칸짜리 + 1칸짜리..라고 생각할 수 있다.
    
    # 1칸짜리들의 합 저장, 2칸짜리 합 저장..n칸짜리 합 저장 순으로 이어나감
    # 합을 더할때 기존의 합들을 저장해두고 이용한다.
    
    # m개의 연속된 수만큼 더하는 행위를 elements 길이만큼 반복하는 것을 한 사이클이라고 할때
    # 이전 사이클에서 저장한 값 + 이어붙일 한칸짜리 값 (얘의 인덱스를 잘 찾아서 더해야 함)
    
    for n in range(length+1): 
        if n == 0 or n == 1:
            continue
        for i in range(length):
            m = (i+n-1)%length      # 이어붙일 한칸짜리 인덱스를 조정하는 작업
            sums.append(sums[(n-2)*length+i] + sums[m]) # 이전사이클 값 + 이어붙일 한칸짜리 값

    answer = len(list(set(sums)))
        
    return answer