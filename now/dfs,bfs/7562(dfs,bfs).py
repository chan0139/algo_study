from collections import deque

def bfs(x,y,e_1,e_2):

    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        if x ==e_1 and y == e_2:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                q.append((nx,ny))
                if nx == e_1 and ny == e_2:
                    break

t = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

while t >= 1:
    n = int(input())
    s_1,s_2 = map(int, input().split())
    e_1,e_2 = map(int, input().split())
    chess = [[0] * (n) for _ in range(n)]

    bfs(s_1,s_2,e_1,e_2)
    print(chess[e_1][e_2])
    t -= 1



