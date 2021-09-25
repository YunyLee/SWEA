import sys
sys.stdin = open('input_5176.txt', 'r')

# [4, 2, 6, 1, 3, 5]
#  1  2(1*2) 4(1*2*2)
#  1     3(1*2+1)
#       3      6
#   2    5

# 1부터 N까지 이진탐색트리 저장
# N이 주어졌을 때, 루트에 저장된값(1번인덱스), N//2번 노드에 저장된 값 출력

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