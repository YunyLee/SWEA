import sys
sys.stdin = open('input_1974.txt', 'r')

def sudoku(ARR):
    global flag

    # 행검사
    for i in range(9):
        cnt = [0] * (9+1)
        for j in range(9):
            cnt[ARR[i][j]] += 1
            if cnt[ARR[i][j]] > 1:
                flag = 0
                return

    # 열검사
    for i in range(9):
        cnt = [0] * (9+1)
        for j in range(9):
            cnt[ARR[j][i]] += 1
            if cnt[ARR[j][i]] > 1:
                flag = 0
                return

    # 3 x 3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = [0] * (9 + 1)
            for x in range(3):
                for y in range(3):
                    cnt[ARR[i+x][j+y]] += 1
                    if cnt[ARR[i+x][j+y]] > 1:
                        flag = 0
                        return

TC = int(input())
for test_case in range(1, TC+1):
    ARR = [list(map(int,input().split())) for _ in range(9)]
    flag = 1 # 0 아니면 1 들어가는 변수

    sudoku(ARR)
    print(f'#{test_case} {flag}')