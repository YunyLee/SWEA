import sys
sys.stdin = open('input_6190.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N= int(input())
    ARR = list(map(int,input().split()))

    temp = set()

    for i in range(N):
        for j in range(i+1, N):
            temp.add(ARR[i] * ARR[j])

    max_num = 0
    for i in temp:
        num = str(i)
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                break
            if int(num) > max_num:
                max_num = int(num)
    print(max_num)
