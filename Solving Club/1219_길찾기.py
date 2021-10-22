import sys
sys.stdin = open('input_1219.txt', 'r')

TC = 10
for test_case in range(1, TC+1):
    TC_NUM, N = map(int,input().split())
    ARR = list(map(int,input().split()))
    result = 0 # 못찾는다고 가정, 찾으면 1 반환

    stack = []

    adjacent_list = [[] for _ in range(100)] # 2차원으로 빈리스트 만들기
    for i in range(0, N, 2):
        adjacent_list[ARR[i]].append(ARR[i+1])

    start = 0 # 0에서부터 시작한다.
    end = 99 # 99를 만나면 길이 존재하는것!

    stack.append(start) # 처음에 0을 넣고 시작한다.
    visited = [0] * 100 # 길의 개수만큼 방문체크 리스트 만든다.

    while stack: # stack에 값이 있을동안 반복
        start = stack.pop()

        if start == end:
            result = 1
            break

        if visited[start]:
            continue
        else:
            visited[start] = 1  # 방문 안했다면 방문체크해주고

        for w in adjacent_list[start]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(test_case, result))