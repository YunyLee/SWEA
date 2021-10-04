import sys
sys.stdin = open('input_2025.txt', 'r')

N = int(input())
sumV = 0
for i in range(1, N+1):
    sumV += i
print(sumV)