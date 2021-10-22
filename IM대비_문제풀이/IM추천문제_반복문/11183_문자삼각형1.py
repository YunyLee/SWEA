import sys
sys.stdin = open('input_11183.txt', 'r')

def fill(arr):
    num = ord('A')
    for i in range(N):
        j = i
        k = N - 1
        while j < N:
            arr[j][k] = chr(num)
            num += 1
            if chr(num) > 'Z':
                num = ord('A')
            k -= 1
            j += 1

def printAll(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[''] * N for _ in range(N)]

    fill(arr)
    print(f'#{tc}')
    printAll(arr)