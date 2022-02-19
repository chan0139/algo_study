
t = int(input())

while t >= 1:
    n = int(input())

    nums = []
    for _ in range(2):
        nums.append(list(map(int, input().split())))

    dp = [[0]*n for _ in range(2)]

    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    for j in range(1,n):
        for i in range(2):
            if i == 0:
                dp[i][j] = max(dp[i+1][j-1] + nums[i][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i][j], dp[i][j-1])
    print(max(dp[0][-1], dp[1][-1]))

    t -= 1
