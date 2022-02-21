import sys

input = sys.stdin.readline

n,r,c = map(int, input().split())



def recursion(i,j,size,check):

    if size == 1:
        if i == r and j == c:
            print(check)
            return
        check += 1
        if i == r and j+1 == c:
            print(check)
            return
        check += 1
        if i+1 == r and j == c:
            print(check)
            return
        check += 1
        if i+1 == r and j+1 == c:
            print(check)
            return
        check += 1


    else:
        new = size -1
        shift = 2 ** new
        if i <= r < i+shift and j <= c < j + shift:
            recursion(i, j, new,check)
        if i <= r < i+shift and j + shift <= c < j + 2**size:
            recursion(i, j+shift, new, check + (shift ** 2) * 1)
        if i + shift <= r < i + 2**size and j <= c < j + shift:
            recursion(i+shift, j, new, check + (shift ** 2) * 2)
        if i + shift <= r < i + 2 ** size and j + shift <= c < j + 2**size:
            recursion(i+shift, j+shift, new, check + (shift ** 2) * 3)

recursion(0,0,n,0)

