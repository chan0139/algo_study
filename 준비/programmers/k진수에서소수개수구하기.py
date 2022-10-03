def get_prime(num):
    convert = int(num)
    div = 2
    if convert == 1:
        return False
    while div * div <= convert:
        if convert % div == 0:
            return False
        div += 1
    return True


def solution(n, k):
    answer = 0
    # k진수 변환
    temp = ''
    while n > 0:
        temp += str(n % k)
        n //= k
    convert = temp[::-1]

    # 0기준으로 스플릿
    convert_split = convert.split('0')
    # print(convert_split)

    # 소수 판별
    for i in convert_split:
        if len(i) > 0:
            check = get_prime(i)
            if check == True:
                answer += 1

    return answer