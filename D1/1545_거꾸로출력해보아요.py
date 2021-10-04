import sys
sys.stdin = open('input_1545.txt', 'r')

N = int(input())
for i in range(N, -1, -1):
    print(i, end=' ')