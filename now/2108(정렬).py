from collections import Counter
import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

list.sort()
a = Counter(list).items()
a = sorted(a, key=lambda items:items[1], reverse=True)
print(round(sum(list)/len(list)))
print(list[len(list)//2])
if len(a) > 1 and a[0][1] == a[1][1]:
    print(a[1][0])
else:
    print(a[0][0])
print(list[-1] - list[0])