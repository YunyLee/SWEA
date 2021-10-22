import sys
sys.stdin = open('input_2105.txt', 'r')

def dfs(x, y, dir, cnt):
    global ans
    # 1. 방향설정
    x = x + dx[dir]
    y = y + dy[dir]

    # 2. 출발점 : ans 갱신 리턴
    if x == sx and y == sy:
        if ans < cnt:
            ans = cnt
        return

    # 3. 인덱스 체크
    if x < 0 or y < 0 or x >= N or y >= N: return
    # 4. 방문 체크
    if visited[arr[x][y]]: return
    # 5. (1) 직진
    #    (2) 방향전환
    visited[arr[x][y]] = 1
    # (1) 직진
    dfs(x, y, dir, cnt + 1)
    # (2) 방향전환
    if dir < 3:
        dfs(x, y, dir + 1, cnt + 1)
    visited[arr[x][y]] = 0


# 우하, 좌하, 좌상, 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 디저트 종류 체크
    visited = [0] * (100 + 1)
    ans = -1

    # 2차원 배열 순회
    for i in range(N):
        for j in range(N):
            sx, sy = i, j
            visited[arr[i][j]] = 1
            dfs(i, j, 0, 1)
            visited[arr[i][j]] = 0

    print(f'#{tc} {ans}')
