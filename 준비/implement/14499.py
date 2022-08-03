n,m,x,y,k = map(int,input().split())

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

commander = list(map(int, input().split()))

# 동1 서2 북3 남4
dx = [0,0,-1,1]
dy = [1,-1,0,0]

dice = [0 for i in range(7)] #초기상태 ceil 1 north 2 east 3 west 4 south 5 floor 6

def turn(move):
    if move == 1:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]
    elif move == 2:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]
    elif move == 3:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]
    else:
        dice[1], dice[2], dice[3], dice[4], dice[5], dice[6] = dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]

for i in range(k):
    move = commander[i]
    nx = x + dx[move-1]
    ny = y + dy[move-1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    turn(move)

    if nums[nx][ny] == 0:
        nums[nx][ny] = dice[6]
    else:
        dice[6] = nums[nx][ny]
        nums[nx][ny] = 0

    x,y = nx, ny
    print(dice[1])





