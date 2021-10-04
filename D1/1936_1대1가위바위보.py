import sys
sys.stdin = open('input_1936.txt', 'r')

A, B = map(int,input().split())

# 가위는 1 바위는 2 보는 3
# 비기는 건 없고, 누가 이겼는지 판별하기
result = ''
#
# if (A+1)%3 == (B%3)

if A == 3 and B == 1:
    result = 'B'
elif A == 1 and B == 3:
    result = 'A'
elif A > B:
    result = 'A'
elif B > A:
    result = 'B'
else: # B == A
    result = '무승부'

print(result)

