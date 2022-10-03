from collections import defaultdict
from collections import Counter

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report) #중복제거
    report_list = []
    report_dicts = defaultdict(int) #신고당한 횟수
    id_dicts = defaultdict(list) #신고한 사람 리스트
    for i in report:
        temp = i.split(' ')
        report_dicts[temp[1]] += 1
        id_dicts[temp[0]].append(temp[1])
    for key,value in report_dicts.items():
        if value >= k: #k번 이상 신고당한 사람의 경우
            for i in range(len(id_list)):
                if key in id_dicts[id_list[i]]: #이 사람이 신고한 리스트에 있는 key인 경우
                    answer[i] += 1 # + 1


    return answer