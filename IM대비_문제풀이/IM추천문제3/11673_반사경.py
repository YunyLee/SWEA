import sys
sys.stdin = open('input_11673.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    row = col = 0

    # 상하좌우 델타 만들기
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 전체행을 돌면서
    for i in range(N):
        for j in range(N):
            if ARR[i][j]: # 거울을 만나면 / 0이 아니면
                row = i
                col = j-1 # 한칸앞 저장
                break # 더 돌 필요가 없으므로 break
        break

    direction = 3 # 한칸앞 0을 저장했으므로 무조건 오른쪽 방향으로 스타트!
    cnt = 0

    while True:
        if 0 <= row < N and 0 <= col < N: #기본 인덱스를 벗어나지 않는다면
            if ARR[row][col] == 1:
                cnt += 1
                # 1. 위에서 내려오던 방향
                if dc[direction] == 0 and dr[direction] == 1:
                    direction = 2

                # 2. 왼쪽에서 오른쪽으로 오던 방향
                elif dc[direction] == 1 and dr[direction] == 0:
                    direction = 0

                # 3. 오른쪽에서 왼쪽으로 오던 방향
                elif dc[direction] == -1 and dr[direction] == 0:
                    direction = 1

                # 4. 아래에서 위로 올라오던 방향
                elif dc[direction] == 0 and dr[direction] == -1:
                    direction = 3

            elif ARR[row][col] == 2:
                cnt += 1
                # 1. 위에서 내려오던 방향
                if dc[direction] == 0 and dr[direction] == 1:
                    direction = 3

                # 2. 왼쪽에서 오른쪽으로 오던 방향
                elif dc[direction] == 1 and dr[direction] == 0:
                    direction = 1

                # 3. 오른쪽에서 왼쪽으로 오던 방향
                elif dc[direction] == -1 and dr[direction] == 0:
                    direction = 0

                # 4. 아래에서 올라오던 방향
                elif dc[direction] == 0 and dr[direction] == -1:
                    direction = 2

            row += dr[direction]
            col += dc[direction]

        else: # 기본 인덱스 방향을 넘어가면 break
            break

    print('#{} {}'.format(test_case, cnt))