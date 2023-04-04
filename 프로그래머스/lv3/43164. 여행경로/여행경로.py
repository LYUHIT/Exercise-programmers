def solution(tickets):
    answer = ["ICN"]
    root = []
    
    def dfs(now, visited, notUsedTickets):
        if len(visited) == len(tickets):
            root.append(visited)
        else:
            for n in tickets:
                if n[0] == now and n in notUsedTickets:
                    newnotUsedTickets = notUsedTickets.copy()
                    newnotUsedTickets.remove(n)
                    newVisited = visited.copy()
                    newVisited.append(n)
                    newnow = n[1]
                    dfs (newnow, newVisited,newnotUsedTickets)
                    
    dfs("ICN",[],tickets)
    root.sort()
    for m in root[0]:
        answer.append(m[1])
    return answer
