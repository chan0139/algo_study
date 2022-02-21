from itertools import combinations

n,m = map(int,input().split())

city = []
for _ in range(n):
    city.append(list(map(int,input().split())))

house = []
chicken = []
result = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])


selects = list(combinations(chicken, m))

for k in selects:
    answer = 0
    for i in house:
        mini = int(1e9)
        for j in k:
            dist = abs(j[0]-i[0]) + abs(j[1]-i[1])
            mini = min(mini, dist)
        answer += mini
    result.append(answer)

print(min(result))
