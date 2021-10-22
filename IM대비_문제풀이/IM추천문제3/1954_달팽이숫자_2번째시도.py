import sys
sys.stdin = open('input_1954.txt', 'r')

# N*N 까지의 숫자 시계방향으로 이루어져 있다.

# 우하좌상

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # N*N크기

    ARR = [[0]*N for _ in range(N)]
    row = col = 0
    direction = 0
    cnt = 1
    ARR[0][0] = 1

    while cnt<N*N:
        row += dr[direction]
        col += dc[direction]
        if 0 <= row < N and 0 <= col < N and ARR[row][col]==0:
            cnt += 1
            ARR[row][col] = cnt
        else:
            row -= dr[direction]
            col -= dc[direction]

            direction = (direction+1)%4

    print(f'#{test_case}')
    for lst in ARR:
        print(*lst)