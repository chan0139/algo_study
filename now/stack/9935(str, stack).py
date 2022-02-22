
string = input()
boom = input()

result = []


for i in string:
    result.append(i)
    if result[-1] == boom[-1] and len(result) >= len(boom):
        if ''.join(result[-len(boom):]) == boom:
            for i in range(len(boom)):
                result.pop()


if len(result) != 0:
    print(''.join(result))

else:
    print("FRULA")







