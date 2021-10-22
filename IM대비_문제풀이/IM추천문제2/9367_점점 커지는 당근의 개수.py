import sys
sys.stdin = open('input_9367.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    CARROT = list(map(int,input().split()))
    cnt = 1
    cnt_list = []

    for i in range(N-1):
        if CARROT[i]+1 == CARROT[i+1]:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1 # 초기화
        cnt_list.append(cnt)

    print('#{} {}'.format(test_case, max(cnt_list)))