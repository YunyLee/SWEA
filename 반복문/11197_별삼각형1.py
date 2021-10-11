import sys
sys.stdin = open('input_11197.txt', 'r')

def one(n):
    global star
    for i in range(1, N+1):
        print(star*i)

def two(n):
    global star
    for i in range(N, 0, -1):
        print(star*i)

def three(n):
    global star
    global blank
    for i in range(1, N*2, 2):
        print(blank*((2*N-i)//2) + star*i + blank*((2*N-i)//2))

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    star = '*'
    blank = ' '

    print('#{}'.format(test_case))
    if M == 1:
        one(N)
    elif M == 2:
        two(N)
    else:
        three(N)