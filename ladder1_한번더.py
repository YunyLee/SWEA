import sys
sys.stdin = open('input_1210.txt', 'r')

TC = 10
M = 100

for test_case in range(1, TC+1):
    N = int(input())
    BOARD = [list(map(int,input().split())) for _ in range(M)]

    start_pos = 0

    dr = [0, 0, 1] # 좌, 우, 하
    dc = [-1, 1, 0] # 좌, 우, 하
    nr = 0
    nc = 0

    for col in range(M):
        if BOARD[nr][nc] == 2:
            break
        if BOARD[0][col] == 1:
            start_pos = col
            row = 0
        while True:
            for i in range(3):
                nr = row + dr[i]
                nc = col + dc[i]
                if 0<= nr <M and 0 <= nc < M:
                    if BOARD[nr][nc] == 1 and dr[i]==0:
                        BOARD[nr][nc] = 3
                        col = nc
                    if BOARD[nr][nc] == 1 and dc[i]==0:
                        BOARD[nr][nc] = 3
                        row = nr
            if BOARD[nr][nc] == 2:
                break

    print('#{} {}'.format(test_case, start_pos))

