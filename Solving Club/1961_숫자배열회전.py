import sys
sys.stdin = open('input_1961.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(str,input().split())) for _ in range(N)]

    angle_90 = list(map(list,zip(*ARR[::-1])))
    angle_180 = list(map(list,zip(*angle_90[::-1])))
    angle_270 = list(map(list,zip(*ARR)))[::-1]

    print('#{}'.format(test_case))
    for i in range(N):
        print(''.join(angle_90[i]), end = ' ')
        print(''.join(angle_180[i]), end = ' ')
        print(''.join(angle_270[i]), end = ' ')
        print()