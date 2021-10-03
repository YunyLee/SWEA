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

    TC = int(input())
    for test_case in range(1, TC + 1):
        STR1 = list(map(str, input()))
        STR2 = list(map(str, input()))
        result = 0
        N = len(STR1)
        M = len(STR2)

        for i in range(M - N + 1):
            if STR1 == STR2[i:i + N]:
                result = 1
                break
            else:
                result = 0

        print('#{} {}'.format(test_case, result))