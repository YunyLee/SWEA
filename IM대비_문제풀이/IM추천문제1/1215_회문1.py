import sys
sys.stdin = open('input_1215.txt', 'r')

def palindrome(lst):
    global cnt
    for i in range(N):
        for j in range(N-M+1):
            temp = lst[i][j:j+M]
            if temp == temp[::-1]:
                cnt += 1

TC = 10
N = 8 # 8*8 평면
for test_case in range(1, TC+1):
    M = int(input()) # 제시된 길이
    ARR = [ list(map(str,input())) for _ in range(N)]
    ARR_axis = list(zip(*ARR)) # 세로를 가로로 축 변경
    cnt = 0

    palindrome(ARR)
    palindrome(ARR_axis)

    print('#{} {}'.format(test_case, cnt))
