import sys
sys.stdin = open('input_1258.txt', 'r')

# 델타 만들기 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def snail_search(row, col):
    global square_list
    row_cnt = col_cnt = 1
    cnt_list = []

    direction = 0
    while True: # 0이 아닌 값이 있으면 계속~~
        row += dr[direction]
        col += dc[direction]

        if 0 <= row < N and 0 <= col < N and ARR[row][col]: #  기본적인 인덱스를 벗어나지 않으면서, 값이 있으면
            if direction == 0:
                col_cnt += 1
            elif direction == 1:
                row_cnt += 1
            ARR[row][col] = 0 # visited마냥 갔던곳의 값을 0으로 만들어준다.
        else: # 인덱스 벗어나거나 값이 0인 곳에 가면
            # 임의로 갔던만큼 다시 돌아오고
            if len(cnt_list) == 0 and direction == 0:  # 처음에만 가로, 세로 길이 측정.
                cnt_list.append(col_cnt)
            elif len(cnt_list) == 1 and direction == 1:
                cnt_list.append(row_cnt)
            row -= dr[direction]
            col -= dc[direction]
            temp_cnt = 0
            direction = (direction + 1) % 4  # 방향 바꿔주기
            # 네방향 탐색하면서 네방향 모두 0이면 끝내기
            for k in range(4):
                if ARR[row+dr[k]][col+dc[k]] == 0:
                    temp_cnt += 1
            if temp_cnt == 4 and len(cnt_list) == 1:
                cnt_list.append(row_cnt)
            if temp_cnt == 4: #4방향 모두 0이면
                square_list.append([cnt_list[1], cnt_list[0]])  # row_cnt 먼저
                return

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [([0] + list(map(int,input().split())) + [0]) for _ in range(N)]
    # 완전 갑옷 두르기
    ARR.insert(0, [0] * (N+2))
    ARR.append([0] * (N+2))

    square_cnt = 0
    square_list = []

    for i in range(N):
        for j in range(N):
            # 전체 탐색을 하면서 0 이 아닌 값을 찾으면 snail_search함수를 실행해라
            if ARR[i][j]:
                square_cnt += 1
                ARR[i][j] = 0 # 0으로 만들어준다.
                snail_search(i, j)

    square_list.sort(key=lambda x:(x[0]*x[1], x[0]))

    print(f'#{test_case} {square_cnt}', end=' ')
    for lst in square_list:
        print(*lst, end = ' ')
    print()


