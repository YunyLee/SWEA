import sys
sys.stdin = open('input_5178.txt', 'r')

# 후위순회
def postorder(root):
    # 아래 두개 더해서 위로 올리는 작업 #
    if root > N:  # root가 갯수보다 큰 경우에
        return 0  # 0으로 return하는 작업

    if tree[root]:  # leaf노드라면 # 이미 값이 들어 있으면
        return tree[root]

    v1 = postorder(root * 2)
    v2 = postorder(root * 2 + 1)
    tree[root] = v1 + v2
    return v1 + v2


'''
    if idx <= 1:
        return
    tree[idx//2] = tree[idx] + tree[idx+1]
    makeTree(idx-2)
'''

T = int(input())

for test_case in range(1, T + 1):
    # 노드의개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    N, M, L = map(int, input().split())
    # 다음 줄부터 M개의 줄에 걸쳐 리프 노드의 번호와 1000이하의 자연수
    tree = [0] * (N + 1)
    for m in range(M):
        leaf, num = map(int, input().split())
        tree[leaf] = num

    postorder(1)

    print('#{} {}'.format(test_case, tree[L]))