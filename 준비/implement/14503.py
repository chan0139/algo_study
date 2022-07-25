n,m = map(int, input().split())
r,c,d = map(int, input().split())

room = []

for i in range(n):
    room.append(list(map(int, input().split())))

visited = [[0]*m for _ in range(n)]
count = 1

#d=0북 d=1동 d=2남 d=3 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def clean(x,y,d):
    visited[x][y] = 1
    global count

    while 1:
        flag = 0
        for _ in range(4):
            nx = x + dx[(d+3)%4]
            ny = y + dy[(d+3)%4]
            d = (d+3)%4
            if room[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                x,y = nx, ny
                count += 1
                flag = 1
                break
        if flag == 0:
            if room[x-dx[d]][y-dy[d]] == 1:
                break
            else:
                x = x-dx[d]
                y = y - dy[d]

clean(r,c,d)
print(count)


