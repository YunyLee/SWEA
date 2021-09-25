import sys
sys.stdin = open('input_1232.txt', 'r')

# 1232 사칙연산

# def calc(v):
#     if len(tree[v])==2:
#         return tree[v][1]
#     else:
#         L = calc(tree[v][2])
#         R = calc(tree[v][3])
#
#         if tree[v][1] == '+': return L+R
#         elif tree[v][1] == '-': return L - R
#         elif tree[v][1] == '*': return L * R
#         elif tree[v][1] == '/': return L / R
#
# for tc in range(1, 11):
#     N = int(input()) # 정점의 개수
#     tree = [0] * (N+1) # 1번정점부터 활용할거라서 N+1
#
#     for i in range(1, N+1):
#         tmp = input().split()
#
#         # 해당번호의 순서대로 들어온다는 보장이 없어서
#         tree[int(tmp[0])] = tmp
#
#         # 입력값을 int로 먼저 처리를 하고가자
#         # tmp의 길이가 4일때, 0번 인덱스 : 정점번호, 1번인덱스 : 연산자
#         # 2번 인덱스 : 왼쪽자식번호 , 3번인덱스 : 오른쪽자식번호
#         if len(tmp) == 4: #길이가 4면 왼쪽자식과 오른쪽자식이 있는 친구다.
#             tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
#             tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
#         else:
#             tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])
#
#     print('#{} {}'.format(tc, int(calc(1))))
#

#########################################################################

def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+':
            return L + R
        elif tree[v][1] == '-':
            return L - R
        elif tree[v][1] == '*':
            return L * R
        elif tree[v][1] == '/':
            return L / R


for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    tree = [0] * (N + 1)  # 1번정점부터 활용할거라서 N+1

    for i in range(1, N + 1):
        tmp = input().split()

        # 해당번호의 순서대로 들어온다는 보장이 없어서
        tree[int(tmp[0])] = tmp

        # 입력값을 int로 먼저 처리를 하고가자
        # tmp의 길이가 4일때, 0번 인덱스 : 정점번호, 1번인덱스 : 연산자
        # 2번 인덱스 : 왼쪽자식번호 , 3번인덱스 : 오른쪽자식번호

    print('#{} {}'.format(tc, int(calc(1))))