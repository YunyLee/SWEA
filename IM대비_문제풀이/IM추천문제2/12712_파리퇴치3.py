import sys
sys.stdin = open('input_12712.txt', 'r')

def kill_flies():
    global max_sum

    # 상 하 좌 우 \위로 /위로 \아래로 /아래로
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]
    for row in range(N):
        for col in range(N):
            sum_value1 = ARR[row][col]
            sum_value2 = ARR[row][col]
            for k in range(8): # 8방향
                for m in range(1, M): # 스프레이 범위
                    nr = row + (dr[k] * m)
                    nc = col + (dc[k] * m)

                    if 0 <= nr < N and 0 <= nc < N:
                        if k < 4: # 가로세로
                            sum_value1 += ARR[nr][nc]
                        else: #대각선
                            sum_value2 += ARR[nr][nc]
            if sum_value1 > max_sum:
                max_sum = sum_value1
            if sum_value2 > max_sum:
                max_sum = sum_value2

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int, input().split()) # NxN배열 M은 스프레이범위
    ARR = [list(map(int,input().split())) for _ in range(N)]
    max_sum = 0

    kill_flies()

    print('#{} {}'.format(test_case, max_sum))