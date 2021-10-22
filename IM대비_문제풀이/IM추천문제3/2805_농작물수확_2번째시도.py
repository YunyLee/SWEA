import sys
sys.stdin = open('input_2805.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input())) for _ in range(N)]
    mid = N // 2
    sum_value = 0

    for i in range(N):
        if i <= mid:
            sum_value += sum(ARR[i][mid-i:N-(mid-i)])
        else:
            sum_value += sum(ARR[i][i-mid:N-(i-mid)])

    print(f'#{test_case} {sum_value}')