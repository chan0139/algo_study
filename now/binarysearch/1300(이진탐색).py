n = int(input())
k = int(input())


left = 1
right = k
answer = 0
while left <= right:
    total = 0
    mid = (left+right)//2
    for i in range(1, n+1):
        total += min(mid // i, n)

    if total < k:
        left = mid + 1
    else:
        right = mid -1
        answer = mid

print(answer)
