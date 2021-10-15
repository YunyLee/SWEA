import sys
sys.stdin = open('input_6485.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 버스 노선 개수
    bus_line_list = []
    for i in range(N):
        A, B = map(int,input().split())
        bus_line_list.append([A,B])
    P = int(input()) # 정류장 개수
    p_list = [] # 정류장 번호 담을 리스트 초기화
    p_cnt_list = [0]*P # 정류장 지나는 노선 개수 담아줄 리스트 초기화
    for i in range(P):
        p_list.append(int(input()))

    for c in range(P): # 정류장 번호들에서 하나씩 꺼내서
        for j in range(N):
            line_A = bus_line_list[j][0]
            line_B = bus_line_list[j][1]
            if line_A <= p_list[c] <= line_B:
                p_cnt_list[c] += 1

    print(f'#{test_case}', *p_cnt_list)