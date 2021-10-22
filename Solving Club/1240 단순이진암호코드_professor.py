import sys
sys.stdin = open('input_1240.txt', 'r')

PATTERN = [
    '0001101', '0011001', '0010011', '0111101', '0100011',
    '0110001', '0101111', '0111011', '0110111', '0001011'
]

TC = int(input())
for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    ARR = [input() for _ in range(N)]

    # 1. 위에서부터 오른쪽 끝지점을 찾는다.
    for row in range(N):
        if '1' in ARR[row]:
            col = ARR[row][::-1].index('1')
            break
    #print(col, row)

    # 2. 코드의 시작점을 계산한다.
    col = M - col - 56
    # print(col)

    # 3. 8개의 숫자를 찾는다.
    res = []
    for i in range(8):
        # print(ARR[row][col:col+7])

        res.append(PATTERN.index(ARR[row][col:col+7]))
        col += 7
    # res = []
    # for i in range(8):
    #     res.append(pattern에서 7개씩 자른 문자열을 사용하여 값을 찾는다.)

    # res검증
    oddS = res[0] + res[2] + res[4] + res[6]
    evenS = res[1] + res[3] + res[5] + res[7]

    if (oddS*3 + evenS) % 10 == 0:
        print('#{} {}'.format(test_case,oddS + evenS))
    else:
        print('#{} {}'.format(test_case,0))