import sys
sys.stdin = open('input_11178.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())

    ARR = [[] for _ in range(N)] # 빈 2차원 리스트를 만든다.

    print('#{}'.format(test_case))

    # 2차원 리스트를 차곡차곡 채워주자
    for i in range(N):
        if i % 2 == 0: #짝수열이면 (0, 2, 4, 6...) 순서대로 넣어주자
            for j in range(65, 65+N):
                ARR[i].append(j + (N*i))
        else: #홀수열이면 (1, 3, 5, 7, ...) 반대로 넣어주자
            for k in range(64+N, 64, -1):
                ARR[i].append(k + (N*i))

    # 열 방향으로 출력하자
    for i in range(N):
        for j in range(N):
            print(chr(ARR[j][i]), end=' ')
        print()


