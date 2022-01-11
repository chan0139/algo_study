k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))



left = 0
right = max(line)
temp = 0
answer = 0
while left <= right:
    temp = 0
    mid = (left+right)//2
    for i in line:
        temp += i // mid

    if temp < n:
        right = mid -1
    else:
        left = mid + 1
        answer = mid

print(answer)


