import sys
sys.stdin = open('input_11159.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    H, W = map(int,input().split())
    temp = 0
    print('#{}'.format(test_case))
    for i in range(1, H+1):
        for j in range(1, W+1):
            j += temp
            print(j, end=' ')
        temp += W
        print()

