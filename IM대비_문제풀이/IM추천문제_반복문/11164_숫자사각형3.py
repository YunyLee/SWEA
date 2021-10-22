import sys
sys.stdin = open('input_11164.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    H, W = map(int,input().split())

    print('#{}'.format(test_case))

    for i in range(H):
        if i % 2 == 0: #짝수번째 행
            for j in range(1, W+1):
                print(j + (W*i), end=' ')
            print()
        else:
            for k in range(W, 0, -1):
                print(k + (W*i), end= ' ')
            print()