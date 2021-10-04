import sys
sys.stdin = open('input_2068.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    NUMBERS = list(map(int,input().split()))

    max_num = 0

    for i in NUMBERS:
        if i > max_num:
            max_num = i

    print('#{} {}'.format(test_case, max_num))