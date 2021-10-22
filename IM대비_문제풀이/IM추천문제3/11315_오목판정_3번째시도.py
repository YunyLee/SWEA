import sys
sys.stdin = open('input_11315.txt', 'r')

def play_omok(lst):
    global result

    # 8방향으로 해도 되지만, 엄밀히 따지면 4방향이 가능하다.
    # 방향이 총 4가지 존재한다. 오른쪽, 아래, \ 대각선 , / 대각선
    dr = [1, 0, 1, -1]
    dc = [0, 1, 1, 1]

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o':
                for k in range(4):  # 4방향
                    cnt = 0  # 방향마다 카운트 초기화
                    for m in range(5):  # 오목은 5개니까
                        nr = i + (dr[k] * m)
                        nc = j + (dc[k] * m)

                        if 0 <= nr < N and 0 <= nc < N:
                            if lst[nr][nc] == 'o':
                                cnt += 1

                        if cnt == 5:
                            result = 'YES'
                            return
    return

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # N*N
    ARR = [list(input()) for _ in range(N)]
    result = 'NO'

    play_omok(ARR)

    print('#{} {}'.format(test_case, result))