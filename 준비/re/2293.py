n,k = map(int, input().split())

c = [int(input()) for i in range(n)]
dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in c:
    for j in range(i,k+1):
            dp[j] += dp[j-i]
            print(dp)

print(dp)

