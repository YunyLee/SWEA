import sys
sys.stdin = open('input_1232.txt', 'r')

# 1232 사칙연산
# 계산결과 출력

def postorder(node):
    if len(tree[node]) == 2:
        return int(tree[node][1])
    elif len(tree[node]) == 4:
        L = postorder(int(tree[node][2])) # 왼쪽
        R = postorder(int(tree[node][3])) # 오른쪽

        # 가운데
        if tree[node][1] == '+':
            return L + R
        elif tree[node][1] == '-':
            return L - R
        elif tree[node][1] == '*':
            return L * R
        elif tree[node][1] == '/':
            return L / R

TC = 10

for test_case in range(1, TC+1):
    N = int(input()) # 정점(노드)의 수
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        temp = input().split()
        tree[int(temp[0])] = temp

    print('#{} {}'.format(test_case, int(postorder(1))))



