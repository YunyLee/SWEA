import sys
sys.stdin = open('input_1983.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int,input().split())
    grade_list = []
    for i in range(N):
        MIDTERM, FINAL, ASSIGNMENT = map(int,input().split())
        result = (MIDTERM * 0.35) + (FINAL * 0.45) + (ASSIGNMENT * 0.2)
        grade_list.append(result)

    K_score = grade_list[K-1]
    grade_list.sort(reverse=True) #성적 내림차순

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    K_index = grade_list.index(K_score)

    answer = grade[K_index // (N//10)]
    print('#{} {}'.format(test_case, answer))