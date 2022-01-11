from bisect import bisect_left, bisect_right
from collections import Counter
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

"""
nums.sort()

def CountNum(array, target):
    left = bisect_left(array, target)
    right = bisect_right(array, target)

    return right-left

for i in check:
    print(CountNum(nums, i), end=' ')

"""
cnt = Counter(nums)
for i in check:
    if i in nums:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
