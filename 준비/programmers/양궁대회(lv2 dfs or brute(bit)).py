
import copy

answer = []        

def dfs(index, info, lion_shot, n):
    global now_max, answer
    if index == 11:
        if n != 0: #인덱스 끝까지 왔는데 기회 남은 경우 -> 남은 기회 0점 처리
            lion_shot[0] = n
        lion = apeach = 0
        for i in range(11):
            if lion_shot[i] > info[i]:
                lion += i
            elif info[i] != 0:
                apeach += i
        if lion > apeach:
            diff = lion - apeach
            if diff > now_max:
                now_max = diff
                answer = copy.deepcopy(lion_shot)
        return
    
    if info[index] < n: #apeach보다 +1발 쏴보는 경우
        temp = copy.deepcopy(lion_shot)
        temp[index] = info[index] + 1
        dfs(index+1, info, temp, n - (info[index]+1))
        temp[index] = 0 #다시 0으로 초기화
    
    #0발 쏘는 경우
    temp2 = copy.deepcopy(lion_shot)
    dfs(index+1, info, temp2, n)

def solution(n, info) :
    global now_max, answer
    info = info[::-1]   #낮은 case 먼저 들어가기 위해서 순서 바꿔줌
    now_max = -1
    dfs(0,info, [0]*11,n)
    if len(answer) > 0:
        return answer[::-1]
    else:
        return [-1]