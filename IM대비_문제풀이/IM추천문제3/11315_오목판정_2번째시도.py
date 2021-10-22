import sys
sys.stdin = open('input_11315.txt', 'r')

# 실패코드2........

def play_omok():
    global result
    cnt1 = cnt2 = cnt3 = cnt4 = 0
    for j in range(N - 5 + 1):
        for i in range(N):
        # 가로 방향
            if ARR[i][j:j+5] == ['o','o','o','o','o']:
                result = 'YES'
                return
        # 세로 방향
            if ARR_axis[i][j:j + 5] == ['o', 'o', 'o', 'o', 'o']:
                result = 'YES'
                return
        # 대각선1 옆 방향
            if ARR[i][i+j] == 'o':
                cnt1 += 1
            else:
                cnt1 = 0
            if ARR[i][N-1-(i+j)] == 'o':
                cnt2 += 1
            else:
                cnt2 = 0
        # 대각선2 아래방향
            if ARR_axis[i][i+j] == 'o':
                cnt3 += 1
            else:
                cnt3 = 0
            if ARR_axis[i][N-1-(i+j)] == 'o':
                cnt4 += 1
            else:
                cnt4 = 0
        # 대각선 오목 판별
            if cnt1 == 5 or cnt2 == 5 or cnt3 == 5 or cnt4 == 5:
                result = 'YES'
                return
    return

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # N*N
    ARR = [list(input()) for _ in range(N)]
    ARR_axis = list(map(list,zip(*ARR)))
    result = 'NO'

    play_omok()

    print('#{} {}'.format(test_case, result))