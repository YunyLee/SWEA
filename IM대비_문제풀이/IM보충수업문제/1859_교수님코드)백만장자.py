import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    DAYS = list(map(int,input().split()))
    max_profit = 0

    for i in range(N-1):
        max_value = DAYS[i]
        # 최대값
        for j in range(i+1, N):
            if max_value < DAYS[j]: 
                max_value = DAYS[j]

        # 최대값 > i값이 크면
        if max_value > DAYS[i]:
            max_profit += max_value - DAYS[i]

    print('#{} {}'.format(test_case, max_profit))