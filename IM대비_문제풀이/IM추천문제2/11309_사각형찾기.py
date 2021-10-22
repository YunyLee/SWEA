import sys
sys.stdin = open('input_11309.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    blank = [0] * N
    max_idx = 0

    for lst in ARR:
        if 1 in lst:
            blank[lst.count(1)]+= 1

    for i in range(len(blank)-1, -1, -1):
        if blank[i] != 0:
            max_idx = i

    result = max_idx * blank[max_idx]

    print('#{} {}'.format(test_case,result))

    # 이 코드는 pass는 했했지만, 2가지 오류가 있다.    # 1. 같은라인에 다른 네모가 존재하는 경우
    # 2. 예를들어 6*5 랑 7*2가 있다면, 이 코드는 7*2가 더 크다고 출력한다.
