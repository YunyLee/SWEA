import sys
sys.stdin = open('input_2058.txt', 'r')

# 자릿수 더하기

N = input()

# 1. str으로 만들어서 더하기
result = 0
for i in N:
    result += int(i)

print(result)