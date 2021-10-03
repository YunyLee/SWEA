import sys
sys.stdin = open('input_4843.txt', 'r')

# 4843 특별한 정렬

# 특별한 정렬을 한 결과를 10개까지 출력하시오

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    NUMBERS = list(map(int, input().split()))

    high_list = sorted(NUMBERS, reverse=True)
    low_list = sorted(NUMBERS)
    result_list = []

    for i in range(len(NUMBERS)//2):
        if len(result_list) < 10 :
            result_list.append(high_list[i])
            result_list.append(low_list[i])

    answer = ''
    for k in result_list:
        answer += str(k) + ' '

    print('#{} {}'.format(test_case, answer))