n = int(input())
i = 0
plus = 0
while True:
    if n <= i:
        break
    plus += 1
    i += plus

if plus % 2 == 0:
    print(str(plus - (i-n)) +'/' + str(1 + (i-n)))
else:
    print(str(1 + (i - n)) + '/' + str(plus - (i-n)))

