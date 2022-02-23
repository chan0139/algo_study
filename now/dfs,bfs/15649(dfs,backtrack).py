
N, M = map(int, input().split())
visited = [False] * (N+1)
nums = []

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, nums)))
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            nums.append(i)
            dfs(depth+1)
            visited[i] = False
            nums.pop()

dfs(0)