n, m = map(int, input().split())
heights = list(map(int, input().split()))

def bisect(array, target, start, end):
    result = []
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                total += i - mid
        if total == target:
            result.append(mid)
            return result
        elif total < target:
            end = mid - 1
        else:
            result.append(mid)
            start = mid + 1
    return result

ans = bisect(heights, m, 0, max(heights))
print(ans[-1])
