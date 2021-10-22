import sys
sys.stdin = open('input_11633.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = list(map(int,input().split()))
    min_sum = 10000*M # a의 최대값인 10000 * M
    max_sum = 0

    for i in range(N-M+1):
        temp = sum(ARR[i:i+M])
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp

    result = max_sum - min_sum
    print('#{} {}'.format(test_case, result))