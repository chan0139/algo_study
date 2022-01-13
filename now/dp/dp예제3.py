n, m = map(int,input().split())

dp = [10001] * 10001
dp[0] = 0
price = []
for i in range(n):
    price.append(int(input()))

for i in range(n):
    for j in range(price[i], m+1):
        if dp[j-price[i]] != 10001:
            dp[j] = min(dp[j], dp[j-price[i]]+1)

print(dp[m])