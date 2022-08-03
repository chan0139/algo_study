
from collections import deque
n,k = map(int, input().split())
shield = deque(map(int, input().split()))


robot = deque([0 for _ in range(len(shield))])

step = 0
while True:
    step +=1
    shield.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    for i in range(n-2,-1,-1):
        if robot[i] != 0:
            if robot[i+1] == 0 and shield[i+1] != 0:
                shield[i+1] -= 1
                robot[i+1], robot[i] = 1, 0
    robot[n-1] = 0

    if robot[0] == 0 and shield[0] > 0:
        shield[0] -= 1
        robot[0] = 1

    count = 0
    for i in range(len(shield)):
        if shield[i] == 0:
            count += 1
    if count >= k:
        print(step)
        break



