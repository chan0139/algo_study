n, m = map(int, input().split())

array = list(map(int, input().split()))

dp = []
index = 0
for i in range(n):
    dp.append(array[index:index+m])
    index += m


for i in range(1,m):
    for j in range(n):
        if j == 0:
            dp[j][i] = max(dp[j][i-1], dp[j+1][i-1]) + dp[j][i]
            continue
        if j == n-1:
            dp[j][i] = max(dp[j-1][i-1], dp[j][i-1]) + dp[j][i]
            continue
        dp[j][i] = max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1]) + dp[j][i]

