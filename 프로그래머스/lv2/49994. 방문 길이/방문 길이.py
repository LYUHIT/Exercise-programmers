def solution(dirs):
    answer = 0
    now = (0,0)
    visited = set()
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    
    for d in dirs :
        if d == "U" and now[1] < 5:
            new = (now[0]+x[0],now[1]+y[0])
            load = ((now[0],now[1]),(new[0],new[1]))
            now = new
            visited.add(load)
        elif d == "D" and now[1] > -5:
            new = (now[0]+x[1],now[1]+y[1])
            load = ((now[0],now[1]),(new[0],new[1]))
            now = new
            visited.add(load)
        elif d == "R" and now[0] < 5:
            new = (now[0]+x[2],now[1]+y[2])
            load = ((now[0],now[1]),(new[0],new[1]))
            now = new
            visited.add(load)
        elif d == "L" and now[0] > -5:
            new = (now[0]+x[3],now[1]+y[3])
            load = ((now[0],now[1]),(new[0],new[1]))
            now = new
            visited.add(load)
            
    answer = len(visited)
    for visit in visited:
        print(visit[1],visit[0])
        if (visit[1],visit[0]) in visited:
            answer -= 0.5

    return answer