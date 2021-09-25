import sys
sys.stdin = open('input_5178.txt', 'r')

def postorder(node):

    if node > N:
        return 0

    if tree[node] != 0:
        return tree[node]

    if node <= N:
        L = postorder(node*2)
        R = postorder((node*2) + 1)

        tree[node] = L + R
        return L + R


TC = int(input())

for test_case in range(1, TC+1):
    N, M, L = map(int,input().split())
    tree = [0] * (N+1)

    for i in range(M):
        LEAF, L_NUM = map(int,input().split())
        tree[LEAF] = L_NUM

    postorder(1)

    print('#{} {}'.format(test_case, tree[L]))