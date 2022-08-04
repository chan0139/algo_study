n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n-1,-1,-1):
    if schedule[i][0] + i <= n:
        dp[i] = max(schedule[i][1]+dp[i+schedule[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]


print(max(dp))


