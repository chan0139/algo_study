import sys
sys.setrecursionlimit(100000)

n = int(input())
area = []
maximum = -1


for _ in range(n):
    area.append(list(map(int, input().split())))
    maximum = max(max(area[-1]), maximum)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x,y,h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visit[nx][ny] or area[nx][ny] <= h:
            continue
        else:
            visit[nx][ny] = True
            dfs(nx,ny,h)

count_list = []

for k in range(0, maximum):
    visit = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j] and area[i][j] > k:
                count += 1
                visit[i][j] = True
                dfs(i,j,k)
    count_list.append(count)

print(max(count_list))


