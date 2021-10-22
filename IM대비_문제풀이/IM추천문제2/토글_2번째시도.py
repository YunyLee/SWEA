import sys
sys.stdin = open('input_12726.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for k in range(1, M+1): # k의 영역은 1부터 M까지
        for i in range(N):
            for j in range(N):
                if M % k == 0: # 전체토글
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1
                elif (i + j +2) % k == 0:
                    if arr[i][j] == 1:
                        arr[i][j] = 0
                    else:
                        arr[i][j] = 1

    for lst in arr:
        cnt += lst.count(1)

    print(f'#{tc} {cnt}')
