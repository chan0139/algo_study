N = int(input())
M = int(input())
min_num = -1
sum = 0
for i in range(N, M+1):
    if i == 1:
        continue
    for j in range(2, i+1):
        if i == j:
            sum += i
            if min_num == -1:
                min_num = i
        if i % j == 0:
            break
if min_num == -1:
    print(-1)
else:
    print(sum)
    print(min_num)