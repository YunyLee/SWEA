import sys
sys.stdin = open('input_2070.txt', 'r')

# 2070 놈놈놈~

TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(int,input().split())

    print('#{}'.format(test_case), end=' ')
    if A > B :
        print('>')
    elif A < B:
        print('<')
    else:
        print('=')