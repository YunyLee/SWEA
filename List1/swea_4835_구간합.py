import sys
sys.stdin = open('input_4835.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    NUMBERS = list(map(int,input().split()))
    result = 0
    max_sum = 0
    min_sum = 100000000

    for i in range(N-M+1):
        temp = sum(NUMBERS[i:i + M])
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp

    result = max_sum - min_sum

    print('#{} {}'.format(test_case, result))