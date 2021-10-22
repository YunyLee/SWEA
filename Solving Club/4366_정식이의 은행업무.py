import sys
sys.stdin = open('input_4366.txt','r')

TC = int(input())

def switch(list, n):
    if list[n] == 0:
        list[n] = 1
    else:
        list[n] = 0

def switch_three_1(list, n):
    if list[n] == 2:
        list[n] = 1
    elif list[n] == 1:
        list[n] = 0
    elif list[n] == 0:
        list[n] = 2

def switch_three_2(list,n):
    if list[n] == 2:
        list[n] = 0
    elif list[n] == 1:
        list[n] = 2
    elif list[n] == 0:
        list[n] = 1

for test_case in range(1, TC+1):
    two = list(map(int,input()))
    three = list(map(int,input()))

    sum_list_two = []
    sum_list_three = []
    bin_list = []
    trd_list = []
    for i in range(1, len(two)+1):
        bin_list.append(2**(len(two)-i))
    for i in range(1, len(three)+1):
        trd_list.append(3**(len(three)-i))

    # 2진수 한자리씩 바꿔서 그 합 저장하기
    for j in range(len(two)):
        sumV = 0
        switch(two, j)
        for i in range(len(two)):
            sumV += bin_list[i]*two[i]
        sum_list_two.append(sumV)
        switch(two, j) # 원래대로 되돌리기

    # 3진수 한자리씩 바꿔서 그 합 저장하기
    for j in range(len(three)):
        sumV = 0
        switch_three_1(three, j)
        for i in range(len(three)):
            sumV += trd_list[i]*three[i]
        sum_list_three.append(sumV)
        switch_three_2(three, j)
        sumV = 0
        switch_three_2(three, j)
        for i in range(len(three)):
            sumV += trd_list[i] * three[i]
        sum_list_three.append(sumV)
        switch_three_1(three, j)

    for i in sum_list_three:
        if i in sum_list_two:
            print('#{} {}'.format(test_case, i))
            break

    print(sum_list_two)
    print(sum_list_three)