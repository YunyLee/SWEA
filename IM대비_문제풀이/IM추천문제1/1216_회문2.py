import sys
sys.stdin = open('input_1216.txt', 'r')

# 회문2

def is_palindrome(lst):

    for length in range(100, 0, -1): # 회문길이 정하기
        for i in range(100): # 행
            cnt = 0
            for j in range(100-length+1):
                temp = lst[i][j:j+length]
                if temp == temp[::-1]:
                    return length

M = 100
TC = 10
for test_case in range(1, TC+1):
    N = int(input())
    ARR = [list(map(str,input())) for _ in range(M)]
    ARR2 = list(zip(*ARR))
    max_cnt = 0

    cnt1 = is_palindrome(ARR)
    cnt2 = is_palindrome(ARR2)
    if cnt1 > cnt2:
        max_cnt = cnt1
    else:
        max_cnt = cnt2

    print('#{} {}'.format(test_case, max_cnt))