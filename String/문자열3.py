import sys
sys.stdin = open('input_4864.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    STR1 = input()
    STR2 = input()
    result = 0

    if STR1 in STR2:
        result = 1

    print('#{} {}'.format(test_case, result))