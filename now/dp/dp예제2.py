n = int(input())
#5로 나누기 , 3으로 나누기 2로 나누기, 1뺴기

# 점화식 = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1

# ex> f(6) -> min(f(5), f(3), f(2)) + 1

dp = [0] * 30001

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[n])