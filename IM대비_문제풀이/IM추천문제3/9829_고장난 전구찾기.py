import sys
sys.stdin = open('input_9829.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    LIGHT, PATTERN = map(int,input().split())
    ARR = [list(map(int,input().split())) for _ in range(PATTERN)]
    normal_light_list = []
    abnormal_light = 0

    for i in range(PATTERN):
        if ARR[i].count(0) == (len(ARR[i])//2)+1: # 0이 절반 이상이면
            for j in range(LIGHT):
                if ARR[i][j] == 1:
                    normal_light_list.append(j+1) # 몇번째 전구인지 인덱스 넣어주기
        else: # 1이 절반 이상이면
            for j in range(LIGHT):
                if ARR[i][j] == 0:
                    normal_light_list.append(j+1)

    normal_set = set(normal_light_list)
    compare_set = set(range(1, LIGHT+1))

    abnormal_light = compare_set - normal_set
    print(f'#{test_case}', *abnormal_light)