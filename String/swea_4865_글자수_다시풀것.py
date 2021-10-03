import sys
sys.stdin = open('input_4865.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    STR1 = input()
    STR2 = input()

    temp = dict()

    STR1 = list(set(STR1))

    for j in STR2:
        for i in STR1:
            if i not in temp.keys() and i == j:
                temp[i] = 1
            elif i in temp.keys() and i == j:
                temp[i] += 1

    print('#{} {}'.format(test_case, temp[max(temp)]))

    print(max(temp))