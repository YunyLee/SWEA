import sys
sys.stdin = open('input_13038.txt', 'r')

TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())
    WEEK = list(map(int, input().split()))  # 일월화수목금토

    temp = WEEK * N
    cnt = 0
    min_day = 0
    for i in temp:
        if cnt == 0 and i == 1:
            cnt += 1
            min_day += 1
        elif cnt != 0 and i == 1:
            cnt += 1
            min_day += 1
        elif cnt != 0 and i == 0:
            min_day += 1
        if cnt == N:
            break

    print('#{} {}'.format(test_case, min_day))

# T = int(input())
#
# for tc in range(1, T+1):
#     target = int(input())
#     cross = list(map(int, input().split()))
#
#     # 주당 수업일수
#     days = cross.count(1)
#
#     # 앞에 붙은 0의 개수 세기
#     cnt = 0
#     for i in range(len(cross)):
#         if cross[i] == 1:
#             break
#         else:
#             cnt += 1
#
#     # 뒤에 붙은 0의 개수 세기
#     for j in range(len(cross)-1, -1, -1):
#         if cross[j] == 1:
#             break
#         else:
#             cnt += 1
#
#
#     result = target // days * 7 - cnt + target % days
#
#     print(f'#{tc} {result}')
