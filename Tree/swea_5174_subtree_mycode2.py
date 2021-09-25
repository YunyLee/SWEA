import sys
sys.stdin = open('input_5174.txt', 'r')

# 노드 N을 루트로 하는 서브트리에 속한 노드의 개수 알아내기

def search(root):
    global cnt
    if tree[0][root] != 0:
        cnt += 1
        search(tree[0][root])
    if tree[1][root] != 0:
        cnt += 1
        search(tree[1][root])

TC = int(input())
for test_case in range(1, TC+1):
    E, N = map(int,input().split())
    NUMBERS = list(map(int,input().split()))
    tree = [[0]*(E+2) for _ in range(2)] # E+1 간선 + 1 = 노드의개수, 거기에 0인덱스까지 포함
    cnt = 1
    # tree[0] = 왼쪽 자식트리
    # tree[1] = 오른쪽 자식트리

    for i in range(0,len(NUMBERS),2):
        if tree[0][NUMBERS[i]] == 0:
            tree[0][NUMBERS[i]] = NUMBERS[i+1]
        else:
            tree[1][NUMBERS[i]] = NUMBERS[i+1]

    # 서브트리의 루트노드 : N
    search(N)
    print('#{} {}'.format(test_case, cnt))
