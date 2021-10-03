import sys
sys.stdin = open('input_4834.txt', 'r')

# 0 ~ 9 까지 N장의 카드

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    CARDS = list(map(int,input()))

    #변수 초기화
    card_num = 0
    cnt = 0
    card_dict = dict()
    max_num = 0

    for i in CARDS:
        if i in card_dict.keys():#값이 있으면
            card_dict[i] += 1
        else:
            card_dict[i] = 1

    for i in card_dict.keys():
        if card_dict[i] >= max_num:
            max_num = card_dict[i]
            if i > card_num:
                card_num = i

    cnt = max(card_dict.values())

    print('#{} {} {}'.format(test_case, card_num, cnt))