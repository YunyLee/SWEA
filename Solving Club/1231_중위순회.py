import sys
sys.stdin = open('input_1231.txt', 'r')

def inorder(root):
    s = tree[root]

    if len(s)>=2: # 왼쪽 노드가 있으면
        inorder(int(s[1]))
    print(s[0], end='')
    if len(s) >= 3: # 오른쪽 노드가 있으면
        inorder(int(s[2]))
    # if root:
    #     inorder(s[1])# inorder(left sub tree 의 root)
    #     print(s[0])
    #     inorder(s[2])# inorder(right sub tree의 root)

TC = 10
for tc in range(1, TC+1):
    print('#{}'.format(tc), end='')

    N = int(input())
    tree = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        s = input().split()
        tree[int(s[0])] = s[1:]
    inorder(1)
    print()