import sys
sys.stdin = open('input_4836.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    BLANK = [[0]*10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        X1, Y1, X2, Y2, COLOR = map(int,input().split())

        for i in range(X1, X2+1):
            for j in range(Y1, Y2+1):
                if BLANK[i][j] == 0:
                    BLANK[i][j] = COLOR
                elif BLANK[i][j] != 0:
                    BLANK[i][j] = 3
                    cnt += 1

    print('#{} {}'.format(test_case, cnt))