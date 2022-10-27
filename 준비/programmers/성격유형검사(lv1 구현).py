from collections import defaultdict

def solution(survey, choices):
    answer = ''
    indicator = defaultdict(int)
    
    
    for i, choice  in enumerate(choices):
        survey_split = list(survey[i]) # AN -> A, N
        #print(survey_split)
        if choice in  [1,2,3]:
            indicator[survey_split[0]] += 4 - choice
        elif choice in [5,6,7]:
            indicator[survey_split[1]] += choice - 4
    #print(indicator)
    for i in range(1,5):
        if i == 1:
            a,b = (indicator['R'], 'R'), (indicator['T'], 'T')
            print(a,b)
        elif i == 2:
            a,b = (indicator['C'], 'C'), (indicator['F'], 'F')
        elif i == 3:
            a,b = (indicator['J'], 'J'), (indicator['M'], 'M')
        else:
            a,b = (indicator['A'], 'A'), (indicator['N'], 'N')
            
        if a[0] >= b[0]:
            answer += a[1]
        else:
            answer += b[1]

        
    
    return answer