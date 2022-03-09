n = int(input())

tower = list(map(int, input().split()))
stack = []
result = []

for i in range(n):

    while stack:
        if stack[-1][1] > tower[i]:
            result.append(stack[-1][0]+1)
            break
        else:
            stack.pop(-1)

    if not stack:
        result.append(0)
    stack.append((i,tower[i]))

for i in result:
    print(i, end = ' ')