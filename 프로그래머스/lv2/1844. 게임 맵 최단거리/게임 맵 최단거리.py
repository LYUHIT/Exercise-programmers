def solution(maps):
    n, m = len(maps)-1, len(maps[0])-1
    answer = 0
    queue = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    queue.append([0,0])
    
    while queue:
        now = queue.pop(0)
        x = now[0]
        y = now[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=n and 0<=ny<=m and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))
    
    destination = maps[n][m]
    
    if destination == 1:
        answer = -1
    else:
        answer = destination
            
    return answer