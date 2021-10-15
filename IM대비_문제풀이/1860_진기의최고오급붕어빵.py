import sys
sys.stdin = open('input_1860.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, M, K = map(int,input().split())
    WAITING = list(map(int,input().split()))
    WAITING.sort() # 온 순서대로 정렬하기
    result = 'Possible'

    for i in range(N):
        # 손님이 도착한 초에 만든 붕어빵 수
        tmp = (WAITING[i]//M) * K
        # tmp- 1(방금 도착한 사람) - i(이전에 도착한 사람)
        # tmp -1 : 현재손님이 가져감, i는 이전손님들이 가져간 수
        if tmp -1 -i < 0:
            result = 'Impossible'
            break

    print(f'#{test_case} {result}')