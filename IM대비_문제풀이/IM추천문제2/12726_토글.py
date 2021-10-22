import sys
sys.stdin = open('input_12726.txt', 'r')

def switch_toggle():
    if ARR[i][j] == 0:
        ARR[i][j] = 1
    else:
        ARR[i][j] = 0

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0

    for k in range(1, M+1): # 1초부터 M초부터
        for i in range(N):
            for j in range(N):
                if M % k == 0:
                    switch_toggle()
                elif 1 <= k < M and (i+j+2) % k == 0:
                    switch_toggle()

    for lst in ARR:
        cnt += lst.count(1)

    print('#{} {}'.format(test_case, cnt))
