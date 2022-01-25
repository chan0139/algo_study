from collections import deque

M, N, H = map(int, input().split())
box = [-1] * H
count = 0

q = deque()

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1]

for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, input().split())))
    box[i] = temp

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append((i,j,k))

def bfs():

    while q:
        x,y,z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dh[i]

            if nx < 0 or nx >= H or ny < 0 or ny >= N or nz < 0 or nz >= M:
                continue
            if box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                q.append((nx,ny,nz))

answer = -1
bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                answer = max(answer, box[i][j][k])

print(answer-1)


