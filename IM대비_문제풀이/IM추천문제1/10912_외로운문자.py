import sys
sys.stdin = open('input_10912.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    word = list(map(str,input()))

    temp = []
    for i in word:
        if i not in temp:
            temp.append(i)
        else:
            temp.pop(temp.index(i))

    temp.sort() # 정렬하고
    result = ''
    for i in temp:
        result += i + ''

    if len(temp) == 0:
        result = 'Good'

    print(f'#{test_case} {result}')
