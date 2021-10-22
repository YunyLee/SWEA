import sys
sys.stdin = open('input_11172.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())

    print('#{}'.format(test_case))

    for i in range(1, N+1):
        for j in range(1, N+1):
            print(i*j, end=' ')
        print()