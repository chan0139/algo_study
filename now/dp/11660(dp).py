import sys

input  = sys.stdin.readline
n,m = map(int, input().split())

nums = []
pos = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

for _ in range(m):
    pos.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

for i in range(n):
    hap = 0
    for j in range(n):
        hap += nums[i][j]
        dp[i][j] = hap
answer = []
for i in range(m):
    x1, y1, x2, y2 = pos[i][0], pos[i][1], pos[i][2], pos[i][3]
    temp = 0
    for j in range(x2-x1+1):
        if y1-2 < 0:
            temp += dp[x1 - 1 + j][y2 - 1]
        else:
            temp += dp[x1-1+j][y2-1] - dp[x1-1+j][y1-1-1]
    answer.append(temp)
for num in answer:
    print(num)

"""
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        nums_sum[x][y] = nums[x - 1][y - 1] + nums_sum[x - 1][y] + nums_sum[x][y - 1] - nums_sum[x - 1][y - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ret = nums_sum[x2][y2] - nums_sum[x1 - 1][y2] - nums_sum[x2][y1 - 1] + nums_sum[x1 - 1][y1 - 1]
    sys.stdout.write(str(ret) + "\n")
"""