import sys
sys.stdin = open('input_4698.txt', 'r')

############# 에라토스 테네스의 체 ################

ARR = [True for _ in range(1000001)] # True로 초기화

ARR[0] = ARR[1] = False # 0, 1은 소수가 아니므로 False로 바꿔준다.

for i in range(int(1000000**0.5)+1): #범위의 제곱근까지..
    if ARR[i]:
        for k in range(2*i, 1000001, i): # 2 * i 하는 이유는 자기자신의 배수부터..
            ARR[k] = False # 범위의 제곱근 이내에 있는 배수는 모두 False로 바꿔줌

###################################################

TC = int(input())
for test_case in range(1, TC+1):
    D, A, B = map(int, input().split())
    cnt = 0

    # 소수 구하기 - 내 예전코드 - 시간초과
    # for i in range(A, B+1):
    #     for j in range(2, int(i**0.5)+1):
    #         if i % j == 0:
    #             break
    #     else:
    for i in range(A, B+1): # A이상 B 이하 범위
        if ARR[i] == True:
            if str(D) in str(i):
                cnt += 1

    print('#{} {}'.format(test_case, cnt))