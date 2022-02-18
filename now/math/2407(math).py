n, m = map(int, input().split())

answer = n
divisor = m
for i in range(1,m):

    answer *= n - i
    divisor *= i


print(answer//divisor)