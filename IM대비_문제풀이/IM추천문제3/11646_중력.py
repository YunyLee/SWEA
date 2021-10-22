import sys
sys.stdin = open('input_11646.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = list(map(int,input().split()))
    max_cnt = 0

    for first_num in range(N):
        cnt = 0
        for compared_num in range(first_num+1, N):
            if ARR[first_num] > ARR[compared_num]:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

    print('#{} {}'.format(test_case, max_cnt))

    # 중력 문제는... 높이가 높은거에 꽂혀서 많이 헤맸던 문제이다.
    # 높이와 관계 없이 모두를 완전탐색 할 수 있도록!!!!
    # 숫자 하나를 꺼내고, 나머지 숫자는 그 다음번에 오는 숫자부터 비교해서
    # 카운트를 쭉 세고 제일 큰 카운트를 반환하면 끝!!!