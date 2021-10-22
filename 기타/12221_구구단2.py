import sys
sys.stdin = open('input_12221.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    A, B = map(int,input().split())

    if 1 <= A < 10 and 1<= B <10:
        print('#{} {}'.format(test_case, A*B))
    else:
        print('#{} {}'.format(test_case, -1))