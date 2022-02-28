from itertools import combinations

n = int(input())

nums = []

for _ in range(n):
    nums.append(list(map(int, input().split())))

team = list(combinations(range(1,n+1), n//2))

mini = int(1e9)

for i in range(len(team)//2):
    temp = team[i]
    team_a = 0
    for j in range(n//2):
        member = temp[j]
        for k in temp:
            team_a += nums[member-1][k-1]

    temp = team[-i-1]
    team_b = 0
    for j in range(n//2):
        member = temp[j]
        for k in temp:
            team_b += nums[member-1][k-1]
    mini = min(mini, abs(team_a - team_b))

print(mini)