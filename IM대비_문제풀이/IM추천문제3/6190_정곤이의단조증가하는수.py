import sys
sys.stdin = open('input_6190.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N= int(input())
    NUMBERS = list(map(int,input().split()))
    multiple_set = set()

    for i in range(N):
        for j in range(i+1, N):
            multiple = str(NUMBERS[i]*NUMBERS[j])
            cnt = 0
            if len(multiple) >= 2:
                for k in range(len(multiple)-1):
                    if int(multiple[k]) <= int(multiple[k+1]):
                        cnt += 1
                if cnt == len(multiple)-1:
                    multiple_set.add(int(multiple))

    if len(multiple_set):
        result = max(multiple_set)
    else:
        result = -1

    print('#{} {}'.format(test_case,result))
