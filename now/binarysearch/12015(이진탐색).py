from bisect import bisect_left

n = int(input())

a = list(map(int, input().split()))
dp = [0]

for i in a:
    k = bisect_left(dp, i)
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[k] = i

print(len(dp)-1)