import sys
sys.stdin = open('input_5176.txt', 'r')

def inorder(root):
    global value
    if root<=N:
        inorder(root*2) #root의 왼쪽 서브트리의 root
    # visit(root)하는거 대신에 value순서대로 넣어라
        tree[root] = value
        value += 1

        inorder(root*2 + 1) #root의 오른쪽 서브트리의 root

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    tree = [0] * (N+1)

    value = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))