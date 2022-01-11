
import sys

n = int(sys.stdin.readline())

pos = list(map(int, sys.stdin.readline().split()))

pos_set = sorted(set(pos))

dic = {pos_set[i]: i for i in range(len(pos_set))}

for i in pos:
    print(dic[i], end=' ')




