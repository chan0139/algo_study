import heapq
import sys
input = sys.stdin.readline
n = int(input())

q = []
while n >= 1:
    temp = int(input())

    if temp == 0:
        if len(q) != 0:
            a, b = heapq.heappop(q)
            if b == -1:
                print(-a)
            else:
                print(a)
        else:
            print(0)
    else:
        if temp < 0:
            heapq.heappush(q, (-temp,-1))
        else:
            heapq.heappush(q, (temp, 1))

    n -= 1