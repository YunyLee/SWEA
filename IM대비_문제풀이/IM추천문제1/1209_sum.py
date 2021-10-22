import sys
sys.stdin = open('input_1209.txt', 'r')



TC = 10
for test_case in range(1, TC+1):
    NUM = int(input())
    N = 100
    ARR = [list(map(int,input().split())) for _ in range(N)]
    ARR_axis = list(map(list,zip(*ARR)))

    max_cnt = 0

    # 가로 세로
    for lst in range(N):
        sum_value = sum_value2 = 0
        sum_value += sum(ARR[lst])
        sum_value2 += sum(ARR_axis[lst])
        if sum_value > max_cnt:
            max_cnt = sum_value
        if sum_value2 > max_cnt:
            max_cnt = sum_value2

    # 대각선
    sum_value3 = sum_value4 = 0
    for i in range(N):
        sum_value3 += ARR[i][i]
        sum_value4 += ARR[i][N-1-i]
    if sum_value3 > max_cnt:
        max_cnt = sum_value3
    if sum_value4 > max_cnt:
        max_cnt = sum_value4

    print('#{} {}'.format(test_case, max_cnt))
