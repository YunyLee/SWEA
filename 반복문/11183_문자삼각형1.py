import sys
sys.stdin = open('input_11183.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N= int(input())

    # 1. 알파벳이 몇개 필요한지 파악하기
    sumV = 0
    sumV_list = []
    for i in range(1, N+1):
        sumV += i
        sumV_list.append(sumV)

    # 2. 빈 배열 만들기
    ARR = [[] for _ in range(N)]

    # 3. 빈 배열에 순서대로 넣기
    temp = 0
    for i in range(N):
        for j in range(N-i):
            ARR[i].append(temp+j+1)
        temp = max(ARR[i])

    # 알파벳을 삼각형 모양으로 배열하기
    print(ARR)
    for i in range(N): # N개의 행
        for j in range(N-i):
            print(ARR[j][i], end=' ')
        print()