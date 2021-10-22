import sys
sys.stdin = open('input_1979.txt', 'r')

def axis(arr):
    arr2 = [[]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr2[i].append(arr[j][i])

    return arr2

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int, input().split())
    ARR = [list(map(str,input().split())) for _ in range(N)]

    result = 0
    for arr in axis(ARR), ARR:
        for lst in arr:
            result += ''.join(lst).split('0').count('1'*K)

    print('#{} {}'.format(test_case, result))
