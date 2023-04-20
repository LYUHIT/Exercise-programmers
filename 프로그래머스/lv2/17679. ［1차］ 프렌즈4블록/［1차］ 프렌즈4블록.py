def solution(m, n, boards):
    board=[]
    for b in boards:
        board.append(list(b))
        
    answer = 0
    combos = []
    blocking = True
    
    while blocking:
        # 블럭 모여있는 것 찾기
        for x in range (m-1):
            for y in range (n-1):
                if board[x][y] != '_' and board[x][y] == board[x+1][y] and board[x][y] == board[x][y+1] and board[x][y] == board[x+1][y+1]:
                    combos.append([x,y])
                    
        if len(combos) == 0:
            blocking = False

        # 블럭 뿌수기
        while combos:
            combo = combos.pop()
            x,y = combo
            board[x][y] = '_'
            board[x+1][y] = '_'
            board[x][y+1] = '_'
            board[x+1][y+1] = '_'

        # 블럭 내리기 (아래부터 순회)
        for x in range (m-2,-1,-1):
            for y in range (n):
                if board[x][y] != '_':
                    nx = x
                    while nx < m-1 and board[nx+1][y] == '_':
                        nx += 1
                    board[x][y],board[nx][y] = board[nx][y],board[x][y]

    # 없어진 블럭 카운트
    for x in range (m):
        for y in range (n):
            if board[x][y] == '_':
                answer += 1
                
    for x in range (m):
        print(board[x])
                
    return answer