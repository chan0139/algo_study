n = int(input())

papers = []
for _ in range(n):
    papers.append(list(map(int, input().split())))

zero = 0
one = 0
minus_one = 0
def get_paper(x,y,n):
    global zero, one, minus_one
    temp = papers[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if papers[i][j] != temp:
                temp = -100
                break
    if temp == -100:
        n = n // 3
        get_paper(x,y,n)
        get_paper(x+n,y,n)
        get_paper(x+2*n,y,n)
        get_paper(x, y+n, n)
        get_paper(x+n, y + n, n)
        get_paper(x + 2 * n, y+n, n)
        get_paper(x, y + 2*n, n)
        get_paper(x+n, y + 2 * n, n)
        get_paper(x + 2*n, y + 2 * n, n)

    elif temp == 0:
        zero += 1
    elif temp == 1:
        one += 1
    elif temp == -1:
        minus_one += 1

get_paper(0,0,n)
print(minus_one)
print(zero)
print(one)




