import sys
sys.stdin = open('input_11168.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    H, W = map(int,input().split())

    print('#{}'.format(test_case))

    for i in range(1, H+1):
        for j in range(i, (W*H)+i, H):
            print(j,end=' ')
        print()