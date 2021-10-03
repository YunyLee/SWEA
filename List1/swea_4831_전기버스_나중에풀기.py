import sys
sys.stdin = open('input_4831.txt')

TC = int(input())

for test_case in range(1, TC+1):
    CAN_GO, N, CHARGER = map(int,input().split())
    CHARGE_STOP = list(map(int,input().split()))

    # 필요한 변수들 초기화(현재위치, 카운트)
    cnt = 0
    current_pos = 0

    while (current_pos + CAN_GO) < N:
        for step in range(CAN_GO, 0, -1):
            if current_pos + step in CHARGE_STOP:
                current_pos += step
                cnt += 1
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(test_case, cnt))