n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n
dp[0] = 1

dpBack = [1] * n
dpBack[0] = 1
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j]+1, dp[i])

nums.reverse()

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dpBack[i] = max(dpBack[j]+1, dpBack[i])
dpBack.reverse()
for i in range(len(dp)):
    dp[i] += dpBack[i]

print(max(dp)-1)
