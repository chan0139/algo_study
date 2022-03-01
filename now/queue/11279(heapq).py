import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
while n >= 1:
    temp = int(input())

    if temp == 0:
        if len(q) != 0:
            print(heapq.heappop(q)*-1)
        else:
            print(0)
    else:
        heapq.heappush(q, -temp)

    n -= 1
