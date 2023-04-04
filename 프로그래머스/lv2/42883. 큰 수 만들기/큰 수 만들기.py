def solution(number, k):
    answer = []
    
    for n in number:
        while k > 0 and answer and answer[-1] < n :
            answer.pop()
            k = k - 1
        answer.append(n)
        
    while k > 0:
        answer.pop()
        k = k - 1
        
    return "".join(answer)