import sys
sys.stdin = open('input_1221.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    T_NUM, N = map(str,input().split())
    GNS = list(map(str,input().split()))

    blank = [0 for _ in range(10)]
    NUM = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    for i in GNS:
        if i == 'ZRO':
            blank[0] += 1
        elif i == 'ONE':
            blank[1] += 1
        elif i == 'TWO':
            blank[2] += 1
        elif i == 'THR':
            blank[3] += 1
        elif i == 'FOR':
            blank[4] += 1
        elif i == 'FIV':
            blank[5] += 1
        elif i == 'SIX':
            blank[6] += 1
        elif i == 'SVN':
            blank[7] += 1
        elif i == 'EGT':
            blank[8] += 1
        elif i == 'NIN':
            blank[9] += 1

    result = ''
    for i in range(len(blank)):
        result += (NUM[i] * blank[i]) + ' '
    print('#{}'.format(test_case))
    print(result)