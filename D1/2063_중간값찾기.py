import sys
sys.stdin = open('input_2063.txt', 'r')

# 2063 중간값 찾기

N = int(input())
NUMBERS = list(map(int,input().split()))

mid = len(NUMBERS) // 2
NUMBERS = sorted(NUMBERS)
print(NUMBERS[mid])