import sys
sys.stdin = open('input_2071.txt', 'r')

# 2071 평균값구하기

TC = int(input())

for test_case in range(1, TC+1):
    TEMP = list(map(int,input().split()))
    sumV = 0

    for i in TEMP:
        sumV += i

    avgV = sumV / len(TEMP)
    print('#{} {}'.format(test_case, round(avgV)))