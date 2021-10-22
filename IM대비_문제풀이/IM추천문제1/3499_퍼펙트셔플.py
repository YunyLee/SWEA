import sys
sys.stdin = open('input_3499.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    CARD = list(map(str,input().split()))
    result_list = []

    if N % 2 == 0:
        temp1 = CARD[:N//2]
        temp2 = CARD[N//2:]

        for i in range(len(temp1)):
            result_list.append(temp1[i])
            result_list.append(temp2[i])

    else:
        temp1 = CARD[:(N//2)+1]
        temp2 = CARD[N//2+1:]

        for i in range(len(temp1)):
            result_list.append(temp1[i])
            if i != len(temp1)-1:
                result_list.append(temp2[i])

    print('#{} {}'.format(test_case, ' '.join(result_list)))