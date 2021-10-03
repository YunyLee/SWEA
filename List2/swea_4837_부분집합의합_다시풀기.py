import sys
sys.stdin = open('input_4837.txt', 'r')

# 부분집합의 합

TC = int(input())

for test_case in range(1, TC+1):
    # N은 부분집합 원소의 수, N_SUM은 부분집합의 합
    N, N_SUM = map(int,input().split())
    cnt = 0

    for i in range(1 << 12): # 1~12까지의 부분집합 2^12
        sum = bitcnt = 0
        for j in range(12): # 0을 12개 초기화?한다는 느낌
            if i & (1 << j):
                sum += j+1 # 0부터니까.. 1부터..하게...?
                bitcnt += 1
        if sum == N_SUM and bitcnt == N:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))