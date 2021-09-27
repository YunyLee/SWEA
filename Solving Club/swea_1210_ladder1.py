import sys
sys.stdin = open('input_1210.txt', 'r')

TC = 10
M = 100

for test_case in range(1, TC+1):
    N = int(input())
    BOARD = [list(map(int,input().split())) for _ in range(M)]

    dr = [0, 0, -1] # 좌 우 상
    dc = [-1, 1, 0]  # 좌 우 상

    result_idx = 0
    start_idx = 0


    for i in range(M):
        if BOARD[M-1][i] == 2:
            start_idx = i

    row = M-1
    col = start_idx
    while True:
        for i in range(3):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < M and 0 <= nc < M:
                if BOARD[nr][nc] == 1 and dr[i] == 0:
                    BOARD[nr][nc] = 2
                    col = nc
                elif BOARD[nr][nc] == 1 and dc[i] == 0:
                    BOARD[nr][nc] = 2
                    row = nr
        if row == 0:
            result_idx = col
            break

    # i == M - 1
    # j = start_idx
    # while True:
    #     for k in range(3):
    #         if dx[k] != 0 and dy[k] == 0 and 0 <= j + dx[k] < M and j != j+dx[k]:
    #             nx = j + dx[k]
    #             ny = i
    #         elif dx[k] == 0 and dy[k] != 0 and 0 <= i + dy[k] < M:
    #             ny = i + dy[k]
    #             nx = j
    #
    #         if BOARD[ny][nx] == 1:
    #             i = ny
    #             j = nx
    #             BOARD[ny][nx] = 2
    #             break
    #
    #     if i == 0:
    #         result_idx = j
    #         break

    print('#{} {}'.format(test_case, result_idx))





