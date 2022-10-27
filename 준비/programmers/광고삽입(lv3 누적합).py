def solution(play_time, adv_time, logs):
    # 시간 초로 변환
    play_time = list(map(int, play_time.split(':')))
    play_time = play_time[0] * 60 * 60 + play_time[1] * 60 + play_time[2]
    total_time = [0] * (play_time + 1)
    adv_time = list(map(int, adv_time.split(':')))
    adv_time = adv_time[0] * 60 * 60 + adv_time[1] * 60 + adv_time[2]

    start_time = 0
    for log in logs:
        temp = log.split('-')
        log_src, log_end = temp[0], temp[1]
        log_src = list(map(int, log_src.split(':')))
        log_src = log_src[0] * 60 * 60 + log_src[1] * 60 + log_src[2]

        log_end = list(map(int, log_end.split(':')))
        log_end = log_end[0] * 60 * 60 + log_end[1] * 60 + log_end[2]
        # print(log_src, log_end)

        # 누적합 계산
        total_time[log_src] += 1
        total_time[log_end] -= 1
    # print(total_time)

    # 누적합 계산
    for i in range(1, play_time):
        total_time[i] += total_time[i - 1]

    # print(total_time)
    now_sum = sum(total_time[:adv_time])
    start_time = 0
    now_max = now_sum

    # 광고 길이 만큼 합 구한다.
    for i in range(adv_time, play_time):
        # 시작지점 빼주고 새로운 지점 더해주면서 값 갱신
        now_sum = now_sum + total_time[i] - total_time[i - adv_time]

        if now_sum > now_max:
            now_max = now_sum
            # 시작지점 개선
            start_time = i - adv_time + 1
    # print(start_time)
    #     print('---------------------------------------')
    #     print(adv_start_list)
    #     print(start_time)
    answer = []
    temp = start_time // 3600
    start_time = start_time % 3600

    if temp < 10:
        temp = '0' + str(temp)
    answer.append(str(temp) + ':')

    temp = start_time // 60
    start_time = start_time % 60
    if temp < 10:
        temp = '0' + str(temp)
    answer.append(str(temp) + ':')
    if start_time < 10:
        start_time = '0' + str(start_time)
    answer.append(str(start_time))
    #     print(start_time)
    #     print(answer)
    answer = ''.join(answer)
    #     print(answer)

    return answer