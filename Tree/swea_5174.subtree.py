import sys
sys.stdin = open('input_5174.txt', 'r')

# 전위순회 pick
def preorder(root):
    # visit(root)
    global cnt
    if root: # root가 가용한 노드인가?:
        cnt += 1
        preorder(tree[root][0])
        preorder(tree[root[1]])


TC = int(input())

for test_case in range(1, TC+1):
    E, N = map(int,input().split())
    S = list(map(int,input().split()))
    tree = [[0,0] for _ in range(E+2)]

    for i in range(0, len(S), 2):
        p, c = S[i], S[i+1]
        if tree[p][0] == 0: #처음나온거면
            tree[p][0] = c
        else:
            tree[p][1] = c

    cnt = 0
    preorder(N)

    print('#{} {}'.format(test_case, cnt))