import sys
sys.stdin = open('input_2005.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())

    pascal = [[0]*N for _ in range(N)]
    pascal[0][0] = 1 # 첫번째줄은 항상 1이다.

    print(f'#{test_case}')

    for i in range(1, N): # 0번째줄은 할 필요가 없다.
        for j in range(N):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j] # 자신의 왼쪽위와 오른쪽위 숫자의 합

    for lst in pascal:
        for i in lst:
            if i:
                print(i, end =' ')
        print()