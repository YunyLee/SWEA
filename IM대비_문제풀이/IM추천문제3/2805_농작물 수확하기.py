import sys
sys.stdin = open('input_2805.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input())) for _ in range(N)]
    sum_value = 0
    mid = N//2

    sum_value += sum(ARR[mid])

    higher, lower, start, end = (mid)-1, (mid)+1, 1, N-1

    while True:
        if higher == -1 and lower == N:
            break
        sum_value += sum(ARR[lower][start:end])
        sum_value += sum(ARR[higher][start:end])
        higher -= 1
        lower += 1
        start += 1
        end -= 1

    print('#{} {}'.format(test_case,sum_value))
