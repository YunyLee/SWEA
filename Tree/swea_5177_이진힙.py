import sys
sys.stdin = open('input_5177.txt', 'r')

def makeT(idx):
    # parent_idx
    if idx==1:
        return

    if tree[idx] < tree[idx//2]: # 부모노드 찾아가고 자식노드 찾아갈때 *2 //2 하는거 주의하기
        tree[idx], tree[idx//2] = tree[idx//2], tree[idx]
        makeT(idx//2)
    # if idx에 있는 데이터의 우선순위 >  부모노드에 있는 데이터를 비교해서 우선순위
    #     교환
    #     다시 재귀로 makeT(부모노드)

def getSum():
    sumV = 0
    idx = N
    while idx>=1:
        sumV += tree[idx]
        idx //= 2
    return sumV

# 재귀로 짜보자
def getSum2(idx):
    global sumV2
    if idx:
        sumV2 += tree[idx]
        getSum2(idx//2)

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    lst = [0] + list(map(int,input().split()))
    tree = [0] * (N+1)
    sumV2 = 0

    for i in range(1, N+1):
        tree[i] = lst[i]
        makeT(i)
    last_node = tree[-1]
    print(getSum2(last_node))
