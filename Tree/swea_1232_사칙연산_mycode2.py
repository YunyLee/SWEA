import sys
sys.stdin = open('input_1232.txt', 'r')

# 연산은 실수로 하되, 결과값 정수로 출력
# 트리 계산결과를 출력하라

def postorder(node):
    if len(tree[node]) == 2: #리프노드라는 뜻, 자식노드가 없다.
        return int(tree[node][1]) # 값을 리턴해서 담아라 L이든 R이든
    elif len(tree[node]) == 4:
        L = postorder(int(tree[node][2]))
        R = postorder(int(tree[node][3]))

        # Left자식과 Right자식을 다 돌아본 뒤에 가운데 루트로 와서 하는일!
        if tree[node][1] == '+':
            return L + R #여기서 int처리 해주지 않는 이유는 계산값이 변할 수 있기 때문
        elif tree[node][1] == '-':
            return L - R
        elif tree[node][1] == '*':
            return L * R
        elif tree[node][1] == '/':
            return L / R
TC = 10
for test_case in range(1, TC+1):
    N = int(input()) # 정점의 수
    tree = [0] * (N+1)
    for i in range(1, N+1):
        temp = input().split()
        node = int(temp[0])
        tree[node] = temp # 노드번호에 맞춰서 값을 다 넣어준다

    print('#{} {}'.format(test_case, int(postorder(1)))) # 1번 정점부터 실행해라