import sys
sys.stdin = open('input_1860.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N, M, K = map(int,input().split()) # N명 M초당 K개
    WAITING = sorted(list(map(int,input().split())))
    cnt = 0
    result = ''

    for i in range(N):
        if WAITING[i] < M:
            result = 'Impossible'
        else:
            for j in range(M, N, M):
                if j >= len(WAITING[(M*K)-1]):
                    result = 'Possible'

    print('#{} {}'.format(test_case, result))