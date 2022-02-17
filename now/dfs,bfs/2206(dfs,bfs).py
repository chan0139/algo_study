from collections import deque

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))

check = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    check[x][y][0] = 1

    while queue:
        x,y,c = queue.popleft()
        if x == n - 1 and y == m-1:
            return check[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0 and check[nx][ny][c] == 0:
                check[nx][ny][c] = check[x][y][c] + 1
                queue.append((nx, ny, c))
            if maps[nx][ny] == 1 and c == 0:
                check[nx][ny][1] = check[x][y][c] + 1
                queue.append((nx, ny, 1))

    return -1

print(bfs(0,0))