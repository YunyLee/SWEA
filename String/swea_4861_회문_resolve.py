import sys
sys.stdin = open('input_4861.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [list(map(str,input())) for _ in range(N)]
    result = ''

    # 가로탐색
    for i in range(N):
        for j in range(N-M+1):
            temp = ARR[i][j:j+M]
            if temp == temp[::-1]:
                result = ''.join(temp)

    # 세로탐색
    for i in range(N):
        for j in range(N-M+1):
            temp = []
            for k in range(M):
                temp.append(ARR[j+k][i])
            if temp == temp[::-1]:
                result = ''.join(temp)

    print('#{} {}'.format(test_case, result))
