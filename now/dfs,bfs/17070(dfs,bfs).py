import sys
input = sys.stdin.readline

n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]

answer = 0

def dfs(i,j,state):
    global answer
    if i == n-1 and j == n-1:
        answer += 1
        return answer

    if state == 0:
        if j+1 < n and house[i][j+1] == 0:
            dfs(i,j+1, 0)
        if i+1 < n and j+1 < n and house[i][j+1] == 0 and house[i+1][j+1] == 0 and house[i+1][j] == 0:
            dfs(i+1,j+1,2)
    if state == 1:
        if i+1 < n and house[i+1][j] == 0:
            dfs(i+1,j,1)
        if i+1 < n and j+1 < n and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0 and house[i + 1][j] == 0:
            dfs(i+1,j+1,2)
    if state == 2:
        if j+1 < n and house[i][j+1] == 0:
            dfs(i,j+1, 0)
        if i+1 < n and house[i+1][j] == 0:
            dfs(i+1,j,1)
        if i+1 < n and j+1 < n and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0 and house[i + 1][j] == 0:
            dfs(i+1,j+1,2)


    return -1

dfs(0,1,0)
print(answer)