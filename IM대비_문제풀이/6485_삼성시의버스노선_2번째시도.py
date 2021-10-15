import sys
sys.stdin = open('input_6485.txt', 'r')

TC = int(input())
for test_case in range(1, TC + 1):
    N = int(input())  # 버스 노선 개수
    a_list = []
    b_list = []
    for i in range(N):
        A, B = map(int, input().split())
        a_list.append(A)
        b_list.append(B)
    P = int(input())
    c_dic = dict()
    for i in range(1, P + 1):
        C = int(input())
        c_dic[C] = 0

    for key in c_dic.keys():
        for i in range(N):
            for j in range(a_list[i], b_list[i] + 1):
                if j == key:
                    c_dic[key] += 1
                    break

    print(f'#{test_case}', *c_dic.values())
