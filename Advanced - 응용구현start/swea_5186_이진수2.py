import sys
sys.stdin = open('input_5186.txt', 'r')

# 5186 이진수2

TC = int(input())

for test_case in range(1, TC+1):
    N = float(input())
    result = ''
    num = N

    for i in range(1, 13): # 12번을 돌거야 13자리 이상은 overflow이기 때문에
        if num >= (0.5 ** i):
            result += str(1)
            num -= (0.5 ** i)
        else:
            result += str(0)
        if num == 0:
            break
        if i == 12 and num !=0:
            result = 'overflow'
            break

    print('#{} {}'.format(test_case, result))


