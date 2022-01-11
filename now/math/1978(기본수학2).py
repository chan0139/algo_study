N = int(input())

nums = map(int, input().split())
answer = 0
for i in nums:
    if i == 1:
        continue
    for j in range(2, i+1):
        if i == j:
            answer += 1
        if i % j == 0:
            break
print(answer)

