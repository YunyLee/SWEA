import sys
sys.stdin = open('input_1926.txt', 'r')

N = int(input())

for i in range(1, N+1):
    temp = str(i)
    cnt = 0
    cnt = temp.count('3') + temp.count('6') + temp.count('9')
    if cnt > 0:
        print('-'*cnt, end =' ')
    else:
        print(i, end = ' ')