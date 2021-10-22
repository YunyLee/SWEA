import sys
sys.stdin = open('input_3143.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    A, B = map(str,input().split())

    temp = list(A)

    for i in range(len(A)-len(B)+1):
        if B == A[i:i+len(B)]:
            for j in B:
                temp.remove(j)

    cnt = (len(A) - len(temp))//len(B)

    result = len(temp) + cnt

    print('#{} {}'.format(test_case, result))
