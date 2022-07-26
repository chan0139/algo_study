import sys
from collections import deque

input = sys.stdin.readline
n,l,r = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    result = []
    result.append((x,y))
    queue.append((x,y))
    visited[x][y]= 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 1:
                continue
            diff = abs(maps[nx][ny] - maps[x][y])
            if diff >= l and diff <= r:
                visited[nx][ny] = 1
                result.append((nx,ny))
                queue.append((nx, ny))

    return result

flag = 0
count = 0

while True:
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                temp = bfs(i,j)
                if len(temp) > 1:
                    flag = 1
                    hap = 0
                    for x,y in temp:
                        hap += maps[x][y]
                    hap = hap // len(temp)
                    for x,y in temp:
                        maps[x][y] = hap
    count += 1
    if flag == 0:
        break

    flag = 0

print(count-1)
