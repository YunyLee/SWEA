import sys
sys.stdin = open('input_11718.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0 # 어차피 사냥꾼이 잡은 전체 마리수이므로, 여기서 초기화
    # 8방향 만들기
    # 상하좌우 \위/위\아래/아래
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]

    # 전체를 탐색하면서
    for row in range(N):
        for col in range(N):
            if ARR[row][col] == 1:
                for k in range(8): # 8방향 탐색하기
                    more = 1 # 델타범위를 늘려줄 변수
                    while True:
                        nr = row + (dr[k] * more)
                        nc = col + (dc[k] * more)
                        if 0 <= nr < N and 0 <= nc < N: # 기본 인덱스를 벗어나지 않고
                            if ARR[nr][nc] == 2: # 토끼를 만났다면 잡자
                                ARR[nr][nc] = 0 # 0으로 바꿔주자
                                cnt += 1
                            elif ARR[nr][nc] == 3:
                                break
                            more += 1
                        else:
                            break

    print('#{} {}'.format(test_case, cnt))
