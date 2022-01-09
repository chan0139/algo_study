import sys

sys.setrecursionlimit(10000)

T = int(input())
result = []
def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if pos[x][y] == 1:
        pos[x][y] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
count = 0
for i in range(T):
    M,N,K = map(int,input().split())
    pos = [[0] * N for _ in range(M)]
    for i in range(K):
        a, b = map(int, input().split())
        pos[a][b] = 1

    for i in range(M):
        for j in range(N):
            if dfs(i,j) == True:
                count += 1

    result.append(count)
    count = 0

for i in result:
    print(i)