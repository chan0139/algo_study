from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    sum1 = sum(deque1)
    sum2 = sum(deque2)
    for i in range(len(queue1) * 3):

        if sum1 > sum2:
            temp = deque1.popleft()
            deque2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum2 > sum1:
            temp = deque2.popleft()
            deque1.append(temp)
            sum1 += temp
            sum2 -= temp
        else:
            return i

    return -1