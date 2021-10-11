import sys
sys.stdin = open('input_11200.txt', 'r')

def one(n):

    for i in range(1, ((N+1)//2)+1):
        mid = (N+1)//2
        if i < mid:
            print(star * i + blank * (mid-i))
        else:
            for j in range(mid,0, -1):
                print(star*j + blank * (mid-j))

def two(n):

    for i in range(1, ((N+1)//2)+1):
        mid = (N+1)//2
        if i < mid:
            print(blank * (mid-i) + star * i)
        else:
            for j in range(mid,0, -1):
                print(blank * (mid-j) + star*j)

def three(n):

    for i in range(N, 0, -2):
        if i > 1:
            print((blank * ((N-i)//2)) + (star*i) + (blank * ((N-i)//2)))
        else:
            for j in range(1, N+1, 2):
                print((blank * ((N-j)//2)) + (star*j) + (blank * ((N-j)//2)))

def four(n):

    for i in range(((N+1)//2), 0, -1):
        mid = (N+1)//2
        if i == 1:
            for j in range(1, mid+1):
                print(blank * (mid-1) + star * j)
        else:
            print(blank * (mid-i) + star * i)


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
    elif M == 3:
        three(N)
    elif M == 4:
        four(N)


