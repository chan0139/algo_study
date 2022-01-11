list = list(map(int, input()))

list = sorted(list, reverse=True)

for i in list:
    print(i, end='')