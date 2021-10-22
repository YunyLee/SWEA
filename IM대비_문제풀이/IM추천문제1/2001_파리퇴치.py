import sys
sys.stdin = open('input_2001.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            for k in range(M):
                sum_value += sum(ARR[i+k][j:j+M])
            if sum_value > max_cnt:
                max_cnt = sum_value

    print('#{} {}'.format(test_case, max_cnt))