n = int(input())
zero = [1,0,1]
one = [0,1,1]
result = []
def fibo(n):

    if n >= len(zero):
        for i in range(len(zero), n+1):
            zero.append(zero[-1] + zero[-2])
            one.append(one[-1] + one[-2])

    result.append((zero[n], one[n]))


for i in range(n):
    fibo(int(input()))

for i in range(len(result)):
    print(result[i][0], result[i][1])