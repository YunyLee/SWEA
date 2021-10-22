import sys
sys.stdin = open('input_4047.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    cards = list(input())
    result = ''

    card_dic = { # 순서대로 딕셔너리를 만든다. (S-D-H-C)
        'S': 13, 'D': 13, 'H': 13, 'C': 13
    }

    temp = []
    card = ''

    for i in range(0,len(cards),3):
        card = ''.join(cards[i:i+3])
        if cards[i+1] == '0':
            card_dic[cards[i]] -= 1
            temp.append(card)
        elif cards[i+1] == '1':
            num = ''.join(cards[i+1:i+3])
            card_dic[cards[i]] -= 1

    if len(temp) == len(set(temp)):
        print(f'#{test_case}', *card_dic.values())
    else:
        print('#{} ERROR'.format(test_case))