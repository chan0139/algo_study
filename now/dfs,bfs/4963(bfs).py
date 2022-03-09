from collections import deque

while 1:
    w,h = map(int, input().split())

    if w == 0 and h == 0:
        break

    island = []
    for _ in range(h):
        island.append(list(map(int, input().split())))

    dx = [-1,1,0,0,1,-1,1,-1]
    dy = [0,0,-1,1,1,-1,-1,1]

    def bfs(x,y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                else:
                    if island[nx][ny] == 1:
                        queue.append((nx,ny))
                        island[nx][ny] = 0

    count = 0
    for i in range(h):
        for j in range(w):
            if island[i][j] == 1:
                count += 1
                island[i][j] = 0
                bfs(i,j)

    print(count)