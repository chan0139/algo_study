def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for i in skill:
        kind, r1, c1, r2, c2, degree = i[0], i[1], i[2], i[3], i[4], i[5]
        if kind == 1: #공격
            # imos 알고리즘 (누적합) 
            temp[r1][c1] -= degree
            temp[r2+1][c2+1] -= degree
            temp[r2+1][c1] += degree
            temp[r1][c2+1] += degree
        else: #회복
            temp[r1][c1] += degree
            temp[r2+1][c2+1] += degree
            temp[r2+1][c1] -= degree
            temp[r1][c2+1] -= degree
    
    #행, 열 훑으면서 더해줌
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i+1][j] += temp[i][j]
    for i in range(len(temp[0])-1):
        for j in range(len(temp)-1):
            temp[i][j+1] += temp[i][j]
    
    #보드와 temp 덧셈
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp[i][j]
            
            if board[i][j] > 0:
                answer += 1
    #print(board)
    return answer