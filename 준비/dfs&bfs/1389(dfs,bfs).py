from collections import deque
import queue
import re

n,m = map(int, input().split())

line = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    line[a][b] = 1
    line[b][a] = 1


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in range(len(line[x])):
            if visited[i] == 0 and line[x][i] == 1:
                visited[i] = visited[x] + 1
                queue.append(i)
visited = [0] * (n+1)
result = []
for i in range(1,n+1):
    bfs(i)
    result.append(sum(visited) - visited[i])
    visited = [0] * (n+1) #방문 초기화
min_result = 5001
answer = 0
for i, number in enumerate(result):
    if number < min_result:
        min_result = min(min_result, number)
        answer = i

print(answer+1)