import sys
sys.stdin = open('input_4522.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    word = input()
    result = 'Not exist'

    cnt = 0

    for i in range(len(word)):
        if word[i] == word[-1-i] or word[i] == '?' or word[-1-i] == '?':
            cnt += 1
        else:
            break

    if cnt == len(word):
        result = 'Exist'

    print('#{} {}'.format(test_case, result))