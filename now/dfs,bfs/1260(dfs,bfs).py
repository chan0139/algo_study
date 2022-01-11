from collections import deque

n,m,v = map(int,input().split())
line = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    line[a][b] = 1
    line[b][a] = 1
visited = [0 for _ in range(n+1)]

def dfs(x):
    print(x, end=' ')
    visited[x] = 1

    for i in range(1, n+1):
        if line[x][i] == 1 and visited[i] == 0:
            dfs(i)
#dfs(v)
visited_2 = [0 for _ in range(n+1)]
def bfs(x):
    queue = deque()
    queue.append(x)
    visited_2[x] = 1
    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in range(n+1):
            if line[temp][i] == 1 and visited_2[i] == 0:
                queue.append(i)
                visited_2[i] = 1

bfs(v)




