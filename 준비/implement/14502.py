from collections import deque
from itertools import combinations
n,m = map(int, input().split())

area = []
blank_area = []
virus = []

for i in range(n):
    area.append(list(map(int, input().split())))
    for j in range(m):
        if area[i][j] == 0:
            blank_area.append((i,j))
        if area[i][j] == 2:
            virus.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(miro):
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    count = 0

    for i, j in virus:
        queue.append((i,j))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if miro[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if miro[i][j] == 0 and visited[i][j] == 0:
                count += 1

    return count

answer = 0
for i,j,k in combinations(blank_area, 3):
    area[i[0]][i[1]] = 1
    area[j[0]][j[1]] = 1
    area[k[0]][k[1]] = 1

    temp = bfs(area)
    answer = max(answer, temp)

    area[i[0]][i[1]] = 0
    area[j[0]][j[1]] = 0
    area[k[0]][k[1]] = 0
    #print(area)

print(answer)