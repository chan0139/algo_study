import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

nums.sort()

left = 0
right = n-1
check = abs(2000000001)
answer_left = 0
answer_right = 0

while left < right:
    mid = nums[left]+nums[right]
    if check > abs(mid):
        check = abs(mid)
        answer_left, answer_right = nums[left], nums[right]

    if mid < 0:
        left += 1
    else:
        right -= 1

print(answer_left,answer_right)

