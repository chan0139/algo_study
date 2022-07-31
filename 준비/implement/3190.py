from collections import deque

n = int(input())
k = int(input())

board = [[0]*(n+1) for _ in range(n+1)]
apple = []
for i in range(k):
    apple.append(list(map(int, input().split())))
    board[apple[i][0]][apple[i][1]] = 1

visited = deque()

move = []
l = int(input())
for _ in range(l):
    x,c = input().split()
    x = int(x)
    move.append((x,c))

curr_pos = 'r'
dx = 0
dy = 1
snake_head = [1,1]

def movement(pos, dir):
    if pos == 'r':
        if dir == 'L':
            nex_pos = 'u'
            dx = -1
            dy = 0
        if dir == 'D':
            nex_pos = 'd'
            dx = 1
            dy = 0
    elif pos == 'l':
        if dir == 'L':
            nex_pos = 'd'
            dx = 1
            dy = 0
        if dir == 'D':
            nex_pos = 'u'
            dx = -1
            dy = 0
    elif pos =='u':
        if dir == 'L':
            nex_pos = 'l'
            dx = 0
            dy = -1
        if dir == 'D':
            nex_pos = 'r'
            dx = 0
            dy = 1
    elif pos =='d':
        if dir == 'L':
            nex_pos = 'r'
            dx = 0
            dy = 1
        if dir == 'D':
            nex_pos = 'l'
            dx = 0
            dy = -1
    return nex_pos, dx, dy

count = 0
i = 0
while True:
    count += 1
    before = [snake_head[0], snake_head[1]]
    snake_head[0] += dx
    snake_head[1] += dy

    if snake_head[0] > n or snake_head[0] <= 0 or snake_head[1] > n or snake_head[1] <= 0:
        print(count)
        #print(curr_pos)
        exit()
    if snake_head in visited:
        print(count)
        #print(curr_pos)
        exit()

    if board[snake_head[0]][snake_head[1]] == 1:
        board[snake_head[0]][snake_head[1]] = 0
        visited.append([before[0], before[1]])
    else:
        visited.append([before[0], before[1]])
        visited.popleft()

    if i < len(move) and count == move[i][0]:
        curr_pos, dx, dy = movement(curr_pos, move[i][1])
        i += 1
