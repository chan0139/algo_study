n,m = map(int, input().split())

visited = [False] * (n+1)
nums = []
result = []

def dfs(depth):
    if depth == m:
        temp = ' '.join(map(str, sorted(nums)))
        if temp not in result:
            result.append(temp)
        return

    for i in range(1,n+1):
        if not visited[i]:
            nums.append(i)
            visited[i] = True
            dfs(depth+1)
            visited[i] = False
            nums.pop()

dfs(0)
for i in result:
    print(i)