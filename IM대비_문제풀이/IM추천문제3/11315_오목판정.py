import sys
sys.stdin = open('input_11315.txt', 'r')

# 처음에 오류코드를 낸 이유 :
# 지엽적인 사고 ㅠㅠ 무조건 N이 5개라고 가정을 하고 코드를 짰다.
# N개라는 점을 잊지말자!! 항상!!


# 실패코드


def play_omok():
    global result
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N-5+1):
        # 가로 방향
            if ARR[i][j:j+5] == ['o','o','o','o','o']:
                result = 'YES'
                return
        # 세로 방향
            if ARR_axis[i][j:j+5] == ['o','o','o','o','o']:
                result = 'YES'
                return

    # 대각선 방향 - 시작점만 ij로 보고 가로 5개 세로 5개
    for k in range(N - 5 + 1):
    # 위 구간 대각선
        for i in range(N):
            if ARR[i][i+k] == 'o':
                cnt1 += 1
            else: # 연속이 안되면 0이되게끔 처리
                cnt1 = 0
            if ARR[i][N-1-(i+k)] == 'o':
                cnt2 += 1
            else:
                cnt2 = 0
        # 대각선 개수 5개되면 yes
            if cnt1 == 5 or cnt2 == 5:
                result = 'YES'
                return

    # 아래 구간 대각선
        for j in range(N):
            if ARR[j+k][j] == 'o':
                cnt1 += 1
            else: # 연속이 안되면 0이되게끔 처리
                cnt1 = 0
            if ARR[N-1-(j+k)][j] == 'o':
                cnt2 += 1
            else:
                cnt2 = 0
        # 대각선 개수 5개되면 yes
            if cnt1 == 5 or cnt2 == 5:
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



