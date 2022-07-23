from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int, input().split())

line = [[0]*(n+1) for _ in range(n+1)]
count = 0
for _ in range(m):
    a,b = map(int, input().split())
    line[a][b] = 1
    line[b][a] = 1
visited = [0] * (n+1)

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        nx = queue.popleft()
        for i in range(1, n+1):
            if line[nx][i] == 1 and visited[i] == 0:
                visited[i] = True
                queue.append(i)



for i in range(1, n+1):
    if visited[i] == 0:
        bfs(i)
        count += 1

print(count)