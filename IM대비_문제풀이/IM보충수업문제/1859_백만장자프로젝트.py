import sys
sys.stdin = open('input_1859.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    DAYS = list(map(int,input().split()))
    max_profit = 0
    temp = []

    for i in range(N-2+1):
        if DAYS[i] <= DAYS[i+1]:
            temp.append(DAYS[i])
            if i == N-2: #  만약 마지막 인덱스이면
                for j in temp:
                    max_profit += DAYS[i+1] - j
        else: # DAYS[i] > DAYS[i+1]
            if len(temp) != 0:
                for j in temp:
                    max_profit += DAYS[i] - j
                temp.clear()

    print('#{} {}'.format(test_case, max_profit))