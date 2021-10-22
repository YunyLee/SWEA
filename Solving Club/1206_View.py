import sys
sys.stdin = open('input_1206.txt', 'r')

TC = 10
for test_case in range(1, TC+1):
    nice_view = 0
    N = int(input())
    BUILDING = list(map(int,input().split()))

    for i in range(2, N-2):
        max_building = 0
        max_building = max(BUILDING[i-2], BUILDING[i-1], BUILDING[i+1], BUILDING[i+2])
        if BUILDING[i] > max_building:
            nice_view += BUILDING[i] - max_building

    print('#{} {}'.format(test_case, nice_view))