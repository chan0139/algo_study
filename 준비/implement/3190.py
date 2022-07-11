from collections import deque

circle = [deque(map(int, input())) for _ in range(4)]
k = int(input())
rotate = []

for _ in range(k):
    rotate.append(list(map(int, input().split())))
result = 0

for i in range(len(rotate)):
    num, direct = rotate[i][0], rotate[i][1]
    num -= 1 # index 조정
    tmp_2 = circle[num][2]  # 비교 대상 저장
    tmp_6 = circle[num][6]
    circle[num].rotate(direct)
    tmp_direct = direct

    # 왼쪽
    direct = tmp_direct
    for i in range(num - 1, -1, -1):
        if circle[i][2] != tmp_6:
            tmp_6 = circle[i][6]
            circle[i].rotate(direct * -1)
            direct *= -1
        else:
            break

    # 오른쪽
    direct = tmp_direct
    for i in range(num + 1, 4):
        if circle[i][6] != tmp_2:
            tmp_2 = circle[i][2]
            circle[i].rotate(direct * -1)
            direct *= -1
        else:
            break

result += circle[0][0] + circle[1][0]*2 + circle[2][0]*4 + circle[3][0]*8


print(result)
