import sys
n = int(sys.stdin.readline())
pos = []
for i in range(n):
    pos.append(list(map(int, sys.stdin.readline().split())))

pos = sorted(pos, key = lambda x: (x[1], x[0]))


for i in range(n):
    print(pos[i][0], end=' ')
    print(pos[i][1])