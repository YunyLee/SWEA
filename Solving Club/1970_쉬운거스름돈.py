import sys
sys.stdin = open('input_1970.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    # 50000, 10000, 5000, 1000, 500, 100, 50, 10
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt = ['', '', '', '', '', '', '', '']

    for i in range(len(money)):
        if N // money[i] >=1:
            money_cnt[i] = str(N // money[i]) + ' '
            N -= (N//money[i])*money[i]
        else:
            money_cnt[i] = str(0) + ' '

    print('#{}'.format(test_case))
    print(''.join(money_cnt))
