import sys
sys.stdin = open('input_1209.txt', 'r')

# swea 1209 sum

TC = 10
M = 100

for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input().split())) for _ in range(M)]

    max_sum = 0
    # 행의 합
    for row in range(M):
        sum_row = 0
        for col in range(M):
            sum_row += ARR[row][col]
        if sum_row > max_sum:
            max_sum = sum_row

    # 열의 합
    for col in range(M):
        sum_col = 0
        for row in range(M):
            sum_col += ARR[row][col]
        if sum_col > max_sum:
            max_sum = sum_col

    # / 대각선 합
    sum_left = 0
    for i in range(M):
        sum_left += ARR[i][i]
    if sum_left > max_sum:
        max_sum = sum_left

    # \ 대각선 합
    sum_right = 0
    for i in range(M):
        sum_right += ARR[i][M-1-i]
    if sum_right > max_sum:
        max_sum = sum_right

    print('#{} {}'.format(test_case, max_sum))