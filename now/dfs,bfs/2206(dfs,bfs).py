from collections import deque

n,m = map(int, input().split())

miro = []
for i in range(n):
    miro.append(list(map(int, input())))

visited = [[[-1]* 2 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y,0))
    visited[0][0][0] = 1

    while q:
        x,y,z = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if miro[nx][ny] == 0 and visited[nx][ny][z] == -1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx,ny,z))
            if z == 0 and miro[nx][ny] == 1 and visited[nx][ny][z] == -1:
                visited[nx][ny][1] = visited[x][y][z] + 1
                q.append((nx,ny,1))

bfs(0,0)
for i in range(n):
    for j in range(m):
        print(visited[i][j][0], end=' ')
    print()

print()
for i in range(n):
    for j in range(m):
        print(visited[i][j][1], end=' ')
    print()