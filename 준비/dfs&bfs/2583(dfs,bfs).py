import sys
sys.setrecursionlimit(100000)

m,n,k = map(int, input().split())

maps = [[0]*n for _ in range(m)]
for i in range(k):
    a,b,c,d = map(int, input().split())
    for i in range(b,d):
        for j in range(a,c):
            maps[i][j] = 1

answer = 0
count = 0
result = []

def dfs(x,y):
    global answer
    if x < 0 or x>=m or y <0 or y >= n:
        return False
    if maps[x][y] == 0:
        maps[x][y] = 1
        answer += 1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

for i in range(m):
    for j in range(n):
        if dfs(i,j) == True:
            count += 1
            result.append(answer)
            answer = 0
result.sort()
print(count)
print(' '.join(map(str, result)))


