import sys
sys.stdin = open('input_11671.txt', 'r')

def find_abc(row, col):
    wave = ord(arr[row][col]) - 64

    for w in range(1, wave+1):
        for direction in range(4): # 상하좌우 4방향이라서 4
            nr = row + (dr[direction] * w)
            nc = col + (dc[direction] * w)

            if 0<=nr<N and 0 <=nc<N and arr[nr][nc] == 'H': # 기본 인덱스 범위에도 들고, H이면
                arr[nr][nc] = 'X' #전파가 닿으면 X로 바꿔주기

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0

    # 델타(상, 하, 좌, 우)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # A는 아스키코드로 65이다.
    # 따라서 64를 빼면 1이 남아서 A는 1 B는 2 C는 3을 출력하게 할 수 있다.

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C':
                find_abc(i, j)

    for lst in arr:
        cnt += lst.count('H')

    print(f'#{test_case} {cnt}')