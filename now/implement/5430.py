t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    flag = True
    array = input()
    nums = []
    temp = ''
    count = 0
    for i in array:

        if i.isdigit():
            temp += i
        else:
            if i != '[' and temp.isdigit():
                nums.append(int(temp))
                temp = ''

    for i in p:

        if i == 'R':
            count += 1
        else:
            if len(nums) == 0:
                print('error')
                flag = False
                break
            else:
                if count % 2 == 0:
                    nums.pop(0)
                else:
                    nums.pop(-1)
    if count %2 != 0:
        nums.reverse()

    if flag == True:
        print(str(list(nums)).replace(' ', ''))

