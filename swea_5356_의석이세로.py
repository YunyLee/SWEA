import sys
sys.stdin = open('input_5356.txt', 'r')

# 2021.09.22

TC = int(input())

for test_case in range(1, TC+1):
    SENTENCE = [list(map(str,input())) for _ in range(5)]
    result_list = []
    len_list = []

    for s in range(5):
        len_list.append(len(SENTENCE[s]))

    max_len = 0
    for k in range(5):
        if len(SENTENCE[k]) > max_len:
            max_len = len(SENTENCE[k])

    for i in range(max_len):
        for j in range(5):
            if len(SENTENCE[j]) > i: # 허락받고 쓰는방법 / try except으로도 가능
                result_list.append(SENTENCE[j][i])

    print('#{} {}'.format(test_case, ''.join(result_list)))