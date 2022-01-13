n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n
dp[0] = 1
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
