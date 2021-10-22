import sys
sys.stdin = open('input_1986.txt', 'r')

# 짝수는 빼기 홀수는 더하기

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    result = 0

    for i in range(1, N+1):
        if i % 2: # 홀수이면
            result += i
        else:
            result -= i

    print(f'#{test_case} {result}')