import sys
sys.stdin = open('input_6485.txt', 'r')

def bus_count(bus_stop):
    cnt = 0

    for j in range(N):
        if a_list[j] <= C <= b_list[j]:
            cnt += 1

    return cnt

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 버스 노선 개수
    a_list = []
    b_list = []
    for i in range(N):
        A, B = map(int,input().split())
        a_list.append(A)
        b_list.append(B)
    P = int(input())
    answer = [] # 버스 수를 저장해 놓을 리스트

    for i in range(1, P+1):
        C = int(input())
        answer.append(bus_count(C))
    # 여기까지 인풋받기 완료

    print(f'#{test_case}', ' '.join(map(str,answer)))