import sys
sys.stdin = open('input_11176.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    temp = N * N

    print('#{}'.format(test_case))
    for i in range(65+temp-1, 65+temp-N-1, -1):
        for j in range(i, 65-1, -N):
            print(chr(j), end=' ')
        print()