import sys
sys.stdin = open('input_2072.txt', 'r')

# 2072 홀수만 더하기

TC = int(input())

for test_case in range(1, TC+1):
    TEMP = list(map(int,input().split()))
    result = 0

    for i in TEMP:
        if i % 2 ==1:
            result += i

    print('#{} {}'.format(test_case, result))