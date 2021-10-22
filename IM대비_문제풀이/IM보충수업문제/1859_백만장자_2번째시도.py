import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    DAYS = list(map(int,input().split()))
    max_profit = 0

    max_value = DAYS[-1]

    for i in range(N-1, -1, -1):
        if DAYS[i] < max_value:
            max_profit += max_value - DAYS[i]
        else:
            max_value = DAYS[i]

    print('#{} {}'.format(test_case, max_profit))