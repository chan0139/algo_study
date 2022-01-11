n = int(input())
m = int(input())
line = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    line[a][b] = line[b][a] = 1
count = 0
visited = [0 for _ in range(n+1)]
def dfs(x):
    global count
    count += 1
    #print(x, end = '')
    visited[x] = 1

    for i in range(n+1):
        if line[x][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)
print(count-1)