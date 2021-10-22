import sys
sys.stdin = open('input_11094.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N= int(input())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    ARR_axis = list(zip(*ARR))
    max_sum = 0
    sum_row = [0] * N
    sum_col = [0] * N

    for i in range(N):
        sum_row[i] = sum(ARR[i]) #각 행마다 합
        sum_col[i] = sum(ARR_axis[i]) # 각 열마다 합

    for i in range(N):
        for j in range(N):
            temp = sum_row[i] + sum_col[j] - ARR[i][j] # 본인은 중복이므로 본인 한번 빼주기
            if temp > max_sum:
                max_sum = temp

    print('#{} {}'.format(test_case, max_sum))