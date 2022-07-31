import sys

input = sys.stdin.readline
t = int(input())

while t > 0:
    flag = 0
    n = int(input())

    nums = []
    for _ in range(n):
        nums.append(input().strip())

    nums.sort(reverse=True)
    flag = 0
    for i in range(len(nums)-1):
        if nums[i].startswith(nums[i+1]):
            flag = 1
            break
    if flag:
        print("NO")
    else:
        print("YES")
    t -= 1






