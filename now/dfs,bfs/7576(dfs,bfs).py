from collections import deque

m,n = map(int, input().split())
box = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for _ in range(n):
    box.append(list(map(int, input().split())))

queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

def bfs():
    global count
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx,ny))


answer = 0
bfs()

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        else:
            answer = max(answer, box[i][j])

print(answer-1)
