import sys
sys.stdin = open('input_11718.txt', 'r')

def find_rabbit(row, col):
    global cnt

    # 델타 이용하기(상, 하, 좌, 우, \좌상 /우상 /좌하 \우하)
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    for direction in range(8): # 8방향 탐색

        nr = row + dr[direction]
        nc = col + dc[direction]

        while True:
            # 배열 안의 인덱스 범위 안에 들어오고 바위도 아니면
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 2:
                    cnt += 1 # 토끼일때만 카운트 증가
                elif arr[nr][nc] == 3 or arr[nr][nc] == 1:
                    break
                nr += dr[direction]
                nc += dc[direction]
            else: # 인덱스를 벗어나면 break
                break

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: # 사냥꾼이면 토끼사냥을 시작하자
                find_rabbit(i, j)

    print(f'#{test_case} {cnt}')