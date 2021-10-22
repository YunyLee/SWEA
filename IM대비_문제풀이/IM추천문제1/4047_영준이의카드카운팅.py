import sys
sys.stdin = open('input_4047.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    card = list(map(str,input()))
    result = ''

    cnt_list = [[] for _ in range(4)]
    for i in range(0, len(card), 3):
        if card[i] == 'S':
            if card[i+1] == '0':
                cnt_list[0].append(card[i+2])
            elif card[i+1] == '1':
                cnt_list[0].append(''.join(card[i+1:i+3]))
        elif card[i] == 'D':
            if card[i+1] == '0':
                cnt_list[1].append(card[i+2])
            elif card[i+1] == '1':
                cnt_list[1].append(''.join(card[i+1:i+3]))
        elif card[i] == 'H':
            if card[i+1] == '0' and card[i+2] not in cnt_list[2]:
                cnt_list[2].append(card[i+2])
            elif card[i+1] == '1':
                cnt_list[2].append(''.join(card[i+1:i+3]))
            else:
                result = 'ERROR'
        elif card[i] == 'C':
            if card[i+1] == '0':
                cnt_list[3].append(card[i+2])
            elif card[i+1] == '1':
                cnt_list[3].append(''.join(card[i+1:i+3]))

    temp = 0
    for lst in cnt_list:
        if len(lst) != 0:
            for i in lst:
                temp = 13-int(i)
                result += str(temp) + ' '
        else:
            result += str(13) + ' '

    print('#{} {}'.format(test_case, result))