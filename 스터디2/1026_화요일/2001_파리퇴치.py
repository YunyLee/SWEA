import sys
sys.stdin = open('input_2001.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    max_cnt = 0

    # 구간합 스러운 부분
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0 # 작은배열 합 더해줄 변수
            for x in range(i, i+M):
                for y in range(j, j+M):
                    cnt += ARR[x][y]
            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{test_case} {max_cnt}')
