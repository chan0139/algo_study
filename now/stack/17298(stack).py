
n = int(input())

nums = list(map(int, input().split()))
stack = []
result = [-1]*n

for i in range(n):

    while stack:
        if stack[-1][0] < nums[i]:
            result[stack[-1][1]] = nums[i]
            stack.pop()
        else:
            stack.append((nums[i], i))
            break
    if not stack:
        stack.append((nums[i], i))



for i in result:
    print(i, end = ' ')