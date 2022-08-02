from collections import deque
n = int(input())

area = []
for _ in range(n):
    area.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            shark_x, shark_y = i,j

area[shark_x][shark_y] = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
shark_size = 2

def bfs(x,y):
    queue = deque()
    distance = []
    queue.append((x,y,0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1

    while queue:
        x,y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] != 0:
                continue
            if area[nx][ny] <= shark_size:
                visited[nx][ny] = 1
                if 0 <= area[nx][ny] <= shark_size:
                    queue.append((nx,ny,dist+1))
                if area[nx][ny] != 0 and area[nx][ny] < shark_size:
                    distance.append((dist+1, nx, ny))
    if distance:
        distance.sort()
        return distance[0]
    else:
        return False
time = 0
eat_count = 0
while True:
    temp = bfs(shark_x,shark_y)

    if temp == False:
        break
    eat_count += 1

    time += temp[0]
    shark_x,shark_y = temp[1], temp[2]
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

    area[shark_x][shark_y] = 0

print(time)