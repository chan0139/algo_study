n = int(input())

stars = [[' '] * (2*n-1) for _ in range(n)]

def star(n,i,j):
    if n == 3:
        stars[j][i] = '*'
        stars[j+1][i-1] = '*'
        stars[j+1][i+1] = '*'
        for k in range(-2,3):
            stars[j+2][k+i] = '*'
    else:
        new = int(n//2)
        star(new,i,j)
        star(new,i-new,j+new)
        star(new,i+new,j+new)
star(n,n-1,0)

for i in stars:
    print(''.join(i))