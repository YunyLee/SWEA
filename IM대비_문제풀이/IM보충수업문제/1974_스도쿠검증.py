import sys
sys.stdin = open('input_1974.txt', 'r')

def garo_sero(lst):

    for i in range(N): #행
        temp = []
        for j in range(N): #열
            if lst[i][j] not in temp:
                temp.append(lst[i][j])
            else:
                return False
    return True

def mini_square(lst):

    for i in range(0,N,3):
        for j in range(0,N,3):
            temp = []
            for k in range(3):
                for m in range(3):
                    if lst[i+k][j+m] not in temp:
                        temp.append(lst[i+k][j+m])
                    else:
                        return False
    return True

TC = int(input())
for test_case in range(1, TC+1):
    N = 9
    ARR = [list(map(int,input().split())) for _ in range(N)]
    ARR_axis = list(zip(*ARR))

    # 가로 세로 미니정사각형 비교
    if garo_sero(ARR) == 1 and garo_sero(ARR_axis) == 1 and mini_square(ARR) == 1:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(test_case, result))