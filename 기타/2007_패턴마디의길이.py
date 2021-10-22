import sys
sys.stdin = open('input_2007.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    SENTENCE = input()

    for i in range(1, 10): # 글자수 1개~ 10개
        if SENTENCE[:i] == SENTENCE[i:i*2]:
            word_length = i
            break

    print('#{} {}'.format(test_case, word_length))