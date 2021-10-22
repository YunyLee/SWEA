import sys
sys.stdin = open('input_1979.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [list(map(str,input().split())) for _ in range(N)]
    answer = 0

    # 행 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            # cnt 증가
            if ARR[i][j] == 1:
                cnt += 1
            # k검사, cnt 초기화
            if ARR[i][j] == 0 or j == N-1:
                if cnt == M:
                    answer += 1
                cnt = 0

    # 열 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            # cnt 증가
            if ARR[j][i] == 1:
                cnt += 1
            # k검사, cnt 초기화
            if ARR[j][i] == 0 or j == N-1:
                if cnt == M:
                    answer += 1
                cnt = 0

    print('#{} {}'.format(test_case, answer))
