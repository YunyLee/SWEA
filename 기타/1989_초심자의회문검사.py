import sys
sys.stdin = open('input_1989.txt', 'r')

# 회문이면 1, 아니면 0을 출력하기

TC = int(input())
for test_case in range(1, TC+1):
    WORD = input()

    if WORD == WORD[::-1]:
        print('#{} {}'.format(test_case, 1))
    else:
        print('#{} {}'.format(test_case, 0))