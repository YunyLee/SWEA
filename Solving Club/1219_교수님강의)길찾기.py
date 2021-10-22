import sys
sys.stdin = open('')

for _ in range(1):
    TC, N = map(int,input().split())
    road = list(map(int,input().split()))

    # 1. 홀짝
    # 2. 2step
    # 3. 2*?

    for i in range(N):
        start = road[2*i]
        end = road[2*i+1]
        print(start,end)

    #######################
    # 저장방법
    # 1. ch1, ch2 (최대길이의 개수가 2개까지라고 했으니까)
    ch1 = [0] * 100
    ch2 = [0] * 100

    for i in range(N):
        if ch1[road[2*i]]==0:
            ch1[road[2*i]] == road[2*i+1]
        else:
            ch2[road[2*i]] = road[2*i+1]

    #  2. 인접행렬
    # 각각의 정점에 2차원 리스트 표현해서 애들의 연결관계 표시

    adj_arr = [[0]*100 for _ in range(100)]
    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    # 3. 인접리스트 방식
    adj_list = [[] for _ in range(100)]
    for i in range(N):
        adj_list[road[2*i]].append(road[2*i+1])

    #인접행렬과 리스트의 차이는 존재한다.


    visited = [0] * 100
    ans = 0

    stack = [0]

    while stack:
        curr = stack.pop()

        if curr == 99:
            ans = 1
            break

        # 방문하지 않았으면

        # 방문했으면 건너가~~
        if visited[curr]: continue # 넘어가
        visited[curr] = 1

        for w in adj_list[curr]:
            if not visited[w]:
                stack.append(w)

    print('#{} {}'.format(test_case,ans))

    ####################################################

def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for i in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS(w)

for _ in range(10):
    tc, N = map(int,input().split())
    road = list(map(int,input().split()))

    adj_arr = [[0]*100 for _ in range(100)]

    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1
    visited = [0] * 100
    ans = 0

    DFS(0)
    print('#{} {}'.format(tc, ans))