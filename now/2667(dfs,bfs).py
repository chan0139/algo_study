n = int(input())
square = []
for i in range(n):
    square.append(list(map(int,input())))

count = 0
num = 0
num_list = []
def dfs(x,y):
    global num
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if square[x][y] == 1:
        num += 1
        square[x][y] = 0

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count += 1
            num_list.append(num)
            num = 0


print(count)
num_list.sort()
for i in num_list:
    print(i)