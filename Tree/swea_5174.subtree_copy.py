import sys
sys.stdin = open('input_5174.txt', 'r')

def subtree(root):
    global cnt
    if left[root] != 0:
        cnt += 1
        subtree(left[root])
    if right[root] != 0:
        cnt += 1
        subtree(right[root])
    if left[root] == 0 and right[root] == 0:
        return cnt

TC = int(input())
for test_case in range(1, TC+1):
    E, N = map(int,input().split()) # E 간선, N 서브트리의 루트노드
    TREE = list(map(int,input().split()))

    left = [0] * (E+2) # 간선+1은 노드개수
    right = [0] * (E+2)

    for i in range(1, len(TREE)): # 노드의 개수만큼 돌자
        if i%2 == 1 and left[TREE[i-1]] == 0:
            left[TREE[i-1]] = TREE[i]
        elif i%2 == 1 and left[TREE[i-1]] != 0:
            right[TREE[i-1]] = TREE[i]

    cnt = 1
    subtree(N)

    print('#{} {}'.format(test_case, cnt))