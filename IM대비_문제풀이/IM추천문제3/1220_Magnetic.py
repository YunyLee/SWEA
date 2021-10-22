import sys
sys.stdin = open('input_1220.txt', 'r')

TC = 10
for test_case in range(1, TC+1):
    M = int(input())
    ARR = [list(map(int,input().split())) for _ in range(M)]

    ARR_axis = list(zip(*ARR)) # 축 반전을 해서
    cnt_list = []
    cnt = 0

    for lst in ARR_axis:
        for i in lst:
            if i == 1 and len(cnt_list) == 0:
                cnt_list.append(1)
            elif i == 2 and len(cnt_list) == 1:
                cnt_list.pop()
                cnt += 1
        cnt_list.clear()

    print('#{} {}'.format(test_case, cnt))