import sys
sys.stdin = open('input_4864.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    STR1 = input()
    STR2 = input()
    m1 = len(STR1)
    m2 = len(STR2)
    result = 0

    for i in range(0,m2-m1+1):
        if STR2[i:i+m1] == STR1:
            result = 1

    print('#{} {}'.format(test_case, result))

    # for i in range(M - N + 1):  # (전체문자열 - 찾을문자열) 길이까지 시작인덱스로 하여 비교
    #     cnt = 0
    #     while cnt < N and w[cnt] == wrd[i + cnt]:  # cnt가 찾을 문자열 길이와 같아지기 전까지 반복   # 한칸씩 가면서 기준 문자와 같을때만 반복
    #         cnt += 1  # 문자열이 같으면 cnt 1을 추가
    #         if cnt == N:  # 찾을 문자열과 길이가 같아졌다면
    #             res = 1  # res 변수 1로 바꾸고  # 함수 사용했다면 res값을 리턴...
    #             break  # while문 종료
    #     if res == 1:  # while문 끝났을 때 res변수가 1인 상태라면
    #         break  # for문 종료  # 함수 사용한다면 이부분은 생략 가능...
    # print(f'#{tc} {res}')