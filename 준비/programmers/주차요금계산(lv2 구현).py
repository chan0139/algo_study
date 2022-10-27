from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    dict_in = defaultdict(tuple)
    dict_min = defaultdict(int)
    # fees -> 기본 시간 / 기본 요금 / 단위 시간 / 단위 요금
    for record in records:
        record_split = record.split(' ')
        time_split = record_split[0].split(':')
        time_min = int(time_split[0]) * 60 + int(time_split[1])
        #print(time_min)
        #print(record_split[2])
        if record_split[2] == 'IN':
            #print(record)
            dict_in[record_split[1]] = (time_min, 1) # 1 -> in 표시
        else:
            dict_min[record_split[1]] += time_min - dict_in[record_split[1]][0]
            dict_in[record_split[1]] = (0,0)
           
    #입차 후 출차 없는 친구들 처리
    for key,value in dict_in.items():
        #print(value[1])
        if value[1] != 0:
            dict_min[key] += (23 * 60 + 59) - value[0]
            
    #주차번호로 정렬
    sort_dict_min = sorted(dict_min.items(), key = lambda item:item[0])
    #print(sort_dict_min)
    
    #주차요금 계산
    for key, value in sort_dict_min:
        if value < fees[0]:
            answer.append(fees[1])
        else:
            plus_time = value - fees[0]
            plus = math.ceil(plus_time / fees[2]) * fees[3] # 추가 요금 계산
            plus += fees[1] #기본 요금 더해줌
            answer.append(plus)
    return answer  