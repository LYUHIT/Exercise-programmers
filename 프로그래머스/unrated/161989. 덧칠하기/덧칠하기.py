def solution(n, m, section):
    answer = 1
    now = section[0]
    
    for s in section : 
        if now + m <= s : 
            now = s
            answer = answer+1
    
    return answer