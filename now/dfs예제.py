N, M = map(int, input().split())

def dfs(i,j):
    if i < 0 or i >= N or j < 0 or j >= M:
        return False
    if graph[i][j] == 0:
        graph[i][j] = 1

        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False

graph = []
for i in range(N):
    graph.append(list(map(int, input())))


count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
print(count)