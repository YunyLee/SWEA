import sys
sys.stdin = open('input_1979.txt', 'r')

def find_word(lst):
    global cnt

    for i in range(N+2):
        temp = 0
        for j in range(N+2):
            if lst[i][j]:
                temp += 1
            else: # 0을 만나면
                if temp == K:
                    cnt += 1
                temp = 0
    return

TC = int(input())
for test_case in range(1, TC+1):
    N, K = map(int,input().split())
    ARR = [([0] + list(map(int,input().split())) + [0]) for _ in range(N)]
    ARR.insert(0, [0]*(N+2))
    ARR.append([0]*(N+2))
    ARR_vertical_axis = list(map(list,zip(*ARR)))
    # 갑옷 두루기, 세로축 전환 완료
    cnt = 0

    find_word(ARR)
    find_word(ARR_vertical_axis)

    print('#{} {}'.format(test_case, cnt))