import sys
sys.stdin = open('input_2043.txt', 'r')

# 서랍의 비밀번호

P, K = map(int,input().split())

cnt = 0

while True:
    if P == K:
        cnt += 1 # 같다고 마지막으로 확인하는 횟수
        break
    if P != K :
        K += 1
        cnt += 1

print(cnt)