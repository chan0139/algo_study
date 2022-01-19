from collections import deque

n,k = map(int, input().split())
check = [0] * 100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            break

        for i in (x-1, x+1, x*2):
            nx = i
            if nx < 0 or nx > 100000:
                continue
            if check[nx] == 0:
                check[nx] = check[x] + 1
                q.append(nx)

bfs(n)
print(check[k])