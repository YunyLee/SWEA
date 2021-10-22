import sys
sys.stdin = open('input_1204.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    ARR = list(map(int,input().split()))

    # 각 점수를 맞은 학생이 몇명인지 표시해줄 리스트 생성하기 (1~100점)
    score = [0] * 101

    for i in range(len(ARR)):
        score[ARR[i]] += 1

    temp = max(score)
    for j in range(len(score)-1, -1, -1):
        if score[j] == temp:
            result = j
            break

    print('#{} {}'.format(test_case, result))