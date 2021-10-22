import sys
sys.stdin = open('input_12004.txt', 'r')

def gugudan():
    global result
    for i in range(1, 10):
        for j in range(1, 10):
            if i*j == N:
                return 'Yes'
    return 'No'

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())

    print('#{} {}'.format(test_case, gugudan()))