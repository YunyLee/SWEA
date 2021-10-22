import sys
sys.stdin = open('input_11183.txt', 'r')

def fill(arr):
    num = ord('A')
    for i in range(N):
        j = 1
        k = N -1
        while j < N:
            arr[j][k] = chr(num)
            num += 1
            if chr(num) > 'Z': # Z보다 커지면 A로 바꾼다.
                num = ord('A')
            k -= 1
            j += 1

def printAll(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [[''] * N for _ in range(N)]

    fill(ARR)
    printAll(ARR)