n = int(input())

target_1, target_2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(x):

    for i in graph[x]:
        if visited[i] == 0:
            print(i)
            visited[i] = visited[x] + 1
            dfs(i)

dfs(target_1)

if visited[target_2] == 0:
    print(-1)
else:
    print(visited)
print(graph)
