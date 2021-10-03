import sys
sys.stdin = open('input_4861.txt', 'r')

# 회문
# N * N 글자판에서 길이가 M인 회문을 찾아 출력하기

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [input() for _ in range(N)]
    result = 0

    # 가로 확인
    for i in range(N):
        for j in range(N-M+1):
            temp = ARR[i][j:j+M]
            if temp == temp[::-1]:
                result = temp

        # 세로 확인 
        for k in range(N-M+1):
            tmp = []
            for j in range(N):
                tmp.append(ARR[i+j][i])
            if tmp == tmp[::-1]:
                result = tmp
                break

    print('#{} {}'.format(test_case, result))