import math

n = int(input())
if n == 1:
    print(1)
else:
    print(math.ceil((-3 + math.sqrt(9 + 12*(n-1)))/6 + 1))