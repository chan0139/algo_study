import sys
sys.setrecursionlimit(100000)

n = int(input())

count = 0
count_2 = 0
pics = []
for _ in range(n):
    pics.append(list(input()))

visited = [[0]*n for _ in range(n)]
visited_2 = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,ver):
    if ver == 0:
        color = pics[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if pics[nx][ny] == color and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx,ny,0)
    if ver == 1:
        color = pics[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if color in ['R', 'G']:
                if pics[nx][ny] in ['R','G'] and visited_2[nx][ny] == 0:
                    visited_2[nx][ny] = 1
                    dfs(nx,ny,1)
            elif color == 'B':
                if pics[nx][ny] =='B' and visited_2[nx][ny] == 0:
                    visited_2[nx][ny] = 1
                    dfs(nx,ny,1)
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i,j,0)
            count += 1
        if not visited_2[i][j]:
            visited_2[i][j] = 1
            dfs(i,j,1)
            count_2 += 1
print(count, count_2)