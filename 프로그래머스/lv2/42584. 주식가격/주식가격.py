def solution(prices):
    length = len(prices)
    answer = []
    
    for p in range(length):
        count = 0
        for i in range(p,length-1):
            if prices[p] <= prices[i]:
                count += 1
            else:
                break
        answer.append(count)
    
    return answer