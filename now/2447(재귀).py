N = int(input())

def star(i,j,n):
    if i % 3 == 1 and j % 3 == 1:
        print(' ', end='')
        return
    elif n == 1:
        print("*", end='')
        return
    else:
        star(i//3, j//3, n//3)

for i in range(N):
    for j in range(N):
        star(i,j,N)
    print('')
