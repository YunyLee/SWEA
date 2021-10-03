import sys
sys.stdin = open('input_4865.txt', 'r')

TC = int(input())

for test_case in range(1, TC+1):
    STR1 = set(input())
    STR2 = input()
    result = 0
    cnt_dict = dict()

    for i in STR1:
        for j in STR2:
            if i == j and i not in cnt_dict.keys():
                cnt_dict[i] = 1
            elif i == j and i in cnt_dict.keys():
                cnt_dict[i] += 1

    result = max(cnt_dict.values())

    print('#{} {}'.format(test_case, result))

# T = int(input())
#
# for tc in range(1, T + 1):
#     str1 = set(input())
#     str2 = list(input())
#
#     strDic = {}
#
#     for s in str1:
#         strDic[s] = str2.count(s)
#
#     print(f'#{tc} {max(strDic.values())}')