from bisect import bisect_left, bisect_right

n, m = map(int, input().split())

nums = list(map(int, input().split()))

left = bisect_left(nums, m)
right = bisect_right(nums, m)
print(right-left)
