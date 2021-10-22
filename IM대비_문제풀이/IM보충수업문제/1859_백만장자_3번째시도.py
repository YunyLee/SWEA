import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    ARR = list(map(int, input().split()))
    max_value = ARR[-1]
    max_profit = 0

    for i in range(N-2, -1, -1):
        if ARR[i] > max_value:
            max_value = ARR[i]
        if ARR[i] <= ARR[i+1]:
            max_profit += max_value - ARR[i]

    print('#{} {}'.format(test_case,max_profit))