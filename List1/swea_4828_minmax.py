import sys
sys.stdin = open('input_4828.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    NUMBERS = list(map(int,input().split()))
    result = 0
    max_num = 1
    min_num = 1000000

    for i in range(N):
        if NUMBERS[i] > max_num:
            max_num = NUMBERS[i]
        if NUMBERS[i] < min_num:
            min_num = NUMBERS[i]

    result = max_num - min_num

    print('#{} {}'.format(test_case, result))