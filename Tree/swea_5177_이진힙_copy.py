import sys
sys.stdin = open('input_5177.txt', 'r')

def makeTree(idx):
    if id == 1: #첫번째 인덱스에서는 부모와 비교할 필요가 없다!!!
        return

    if tree[idx] < tree[idx//2]: # 부모노드보다 현재 노드의 값이 더 작으면 교환해줘
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx] # 교환
        makeTree(idx//2) # 재귀 # 부모노드로...


def getSum():
    sumV = 0
    idx = N//2
    while idx >= 1: # 인덱스가 1보다 크거나 같은 동안 # 재귀로 해도 되지만 재귀 아닌 반복문으로 구현
    # for i in range(N, 0, -1):
        sumV += tree[idx] #부모노드의 값을 합산한다
        idx //= 2
    return sumV


TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    tree = [0] * (N+1)

    for i in range(1, N+1): # 2진 힙을 만드는 과정
        tree[i] = lst[i]
        makeTree(i)

    print('#{} {}'.format(test_case, getSum()))