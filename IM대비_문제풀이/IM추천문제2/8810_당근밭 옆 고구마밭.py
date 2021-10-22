import sys
sys.stdin =open('input_8810.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = list(map(int,input().split()))

    longest_stem = 0
    cnt = 0
    sumV = ARR[0]
    sweet_potato = {}

    for i in range(N-1):
        if ARR[i] < ARR[i+1]:
            sumV += ARR[i+1]
            cnt += 1
        else:
            if cnt >=1:
                longest_stem += 1
                if cnt in sweet_potato.keys():
                    if sweet_potato[cnt] < sumV:
                        sweet_potato[cnt] = sumV
                else:
                    sweet_potato[cnt] = sumV
                cnt = 0
                sumV = ARR[i+1]
    if cnt>=1:
        longest_stem += 1
        if cnt in sweet_potato.keys():
            if sweet_potato[cnt] < sumV:
                sweet_potato[cnt] = sumV
        else:
            sweet_potato[cnt] = sumV

    temp = max(sweet_potato.keys())
    result = sweet_potato[temp]

    print(f'#{test_case} {longest_stem} {result}')