import sys
sys.stdin = open('input_1208.txt', 'r')

TC = 10

for test_case in range(1, TC+1):
    N = int(input()) # 덤프횟수
    BOX = list(map(int,input().split())) # 상자높이
    result = 0

    for i in range(N):
        max_index = BOX.index(max(BOX))
        min_index = BOX.index(min(BOX))
        BOX[max_index] -= 1
        BOX[min_index] += 1
        if max(BOX) - min(BOX) <= 1:
            break
    result = max(BOX) - min(BOX)

    print('#{} {}'.format(test_case, result))