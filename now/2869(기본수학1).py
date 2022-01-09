import math
A,B,V = map(int,input().split())


day = math.ceil((V-A) / (A-B))
print(day+1)
