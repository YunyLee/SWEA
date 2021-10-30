import sys
sys.stdin = open('input_11315.txt', 'r')

def find_omok(row, col):
    global result
    # 돌만 발견하면 4방향 탐색하기

    if result == 'YES': #이미 yes인 결과에 대해서 더 진행하지 않기
        return

    # 우, 하, 우하\, 좌하/
    dr = [0, 1, 1, 1]
    dc = [1, 0, 1, -1]

    for direction in range(4):
        cnt = 1 # 이미 돌 찾은거부터 시작이니까
        nr = row + dr[direction]
        nc = col + dc[direction]

        while True:
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 'o': # 범위 내에 있거나, 오목돌이라면
                cnt += 1
                nr += dr[direction]
                nc += dc[direction]
            else:
                break # 그게 아니라면 더 볼 필요가 없다. 다음 direction으로 가자
            if cnt == 5:
                result = 'YES'
                return

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                find_omok(i, j)

    print(f'#{test_case} {result}')