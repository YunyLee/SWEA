import sys
sys.stdin = open('input_11671.txt', 'r')

def find_base_station(lst, row, col, k): # k는 곱하는 횟수

    # 상하좌우 델타
    dr = [-1, 1, 0, 0] # 상하
    dc = [0, 0, -1, 1] # 좌우

    for d in range(4): #상하좌우 4번
        nr = row + (dr[d] * k)
        nc = col + (dc[d] * k)

        if 0 <= nr <N and 0 <= nc < N:
            if lst[nr][nc] == 'H':
                lst[nr][nc] = 'X'

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(input()) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if ARR[i][j] == 'A':
                for k in range(1):
                    find_base_station(ARR, i, j, k+1)
            elif ARR[i][j] == 'B':
                for k in range(2):
                    find_base_station(ARR, i, j, k+1)
            elif ARR[i][j] == 'C':
                for k in range(3):
                    find_base_station(ARR, i, j, k+1)

    for lst in ARR:
        cnt += lst.count('H')
    print('#{} {}'.format(test_case, cnt))