def solution(k, dungeons):
    visited = set()
    answer = -1
    queue = []
    maps = len(dungeons)
    
    for d in dungeons:
        queue.append([k-d[1], 1 << dungeons.index(d), 1])
        visited.add((d[0], 1 << dungeons.index(d)))
        
    while queue:
        thisTime = queue.pop(0)
        nowHP = thisTime[0]
        visitedDungeons = thisTime[1]
        clear = thisTime[2]
        
        if clear > answer:
            answer = clear
            
        for i,d in enumerate(dungeons):
            if not visitedDungeons & (1 << i) and nowHP >= d[0]:
                newHP = nowHP - d[1]
                newVisited = visitedDungeons | (1 << i)
                newClear = clear + 1
                if (newHP, newVisited) not in visited:
                    visited.add((newHP, newVisited))
                    queue.append([newHP, newVisited, newClear])
                
    return answer
