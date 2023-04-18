def solution(m, n, puddles):
    answer = 0
    maps = []
    for _ in range(n):
        maps.append([ 0 for _ in range(m) ])
    maps[0][0] = 1
    
    print(maps)
    
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] not in puddles :
                if i == 0 and j == 0:
                    continue
                elif i < 1 :
                    maps[i][j] = + maps[i][j-1]
                
                elif j < 1 : 
                    maps[i][j] = maps[i-1][j]
                    
                else:
                    maps[i][j] = (maps[i-1][j] + maps[i][j-1]) % 1000000007
                
    print(maps)
    
    answer = maps[-1][-1]
    
    return answer