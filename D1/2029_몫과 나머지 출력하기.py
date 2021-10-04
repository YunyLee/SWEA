import sys
sys.stdin = open('input_2029,txt', 'r')

# 몫과 나머지 출력하기
TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(int,input().split())
    m = n = 0

    m = A // B
    n = A % B

    print('#{} {} {}'.format(test_case, m, n))

