n, m = map(int, input().split())

heights = list(map(int, input().split()))

left = 1
right = max(heights)
answer = 0
while left <= right:
    total = 0
    mid = (left+right)//2
    for i in heights:
        if i > mid:
            total += i - mid
    if total < m:
        right = mid - 1

    else:
        left = mid + 1
        answer = mid

print(answer)