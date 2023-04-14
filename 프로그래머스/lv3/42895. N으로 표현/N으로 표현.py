def solution(N, number):
    answer = -1
    
    queue = [5]
    counts = [[],[N],[N*11,N+N,N/N,N*N],[],[],[],[],[],[],[]]
    
    if number in counts[1]:
        return 1
    if number in counts[2]:
        return 2
              
    for n in range(3,9):
        counts[n].append(int(str(N)*n))
        for i in range(1,n):
            for j in range(n-i,1, -1):
                for a in counts[i]:
                    for b in counts[j]:
                        for c in [a+b,a-b,a*b,a//b,b-a,b//a]:
                            if c > 0 :
                                if c == number:
                                    return n
                                else: 
                                    counts[n].append(c)        
    return answer