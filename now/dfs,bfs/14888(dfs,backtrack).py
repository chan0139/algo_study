n = int(input())

nums = list(map(int, input().split()))
operations = list(map(int, input().split()))

mini = int(1e9)
maxi = -int(1e9)

def dfs(depth, result, plus, minus, mul, div):
    global mini, maxi
    if depth == n-1:
        mini = min(result, mini)
        maxi = max(result, maxi)
        return
    else:
        if plus > 0:
            dfs(depth + 1, result + nums[depth + 1], plus - 1, minus, mul, div)
        if minus > 0:
            dfs(depth + 1, result - nums[depth + 1], plus, minus-1, mul, div)
        if mul > 0:
            dfs(depth + 1, result * nums[depth + 1], plus, minus, mul-1, div)
        if div > 0:
            if result < 0:
                dfs(depth + 1, -(abs(result) // nums[depth + 1]), plus, minus, mul, div-1)
            else:
                dfs(depth + 1, result // nums[depth + 1], plus, minus, mul, div - 1)
dfs(0, nums[0], operations[0], operations[1], operations[2], operations[3])
print(maxi)
print(mini)




