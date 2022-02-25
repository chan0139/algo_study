n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
visited = [False] * (n+1)
answer = []
def dfs(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return

    else:
        for i in range(len(nums)):
            if not visited[i]:
                answer.append(nums[i])
                visited[i] = True
                dfs(depth+1)
                visited[i] = False
                answer.pop()

dfs(0)
