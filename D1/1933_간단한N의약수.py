import sys
sys.stdin = open('input_1933.txt', 'r')

# 약수 나눠서 나머지가 0인거!

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')