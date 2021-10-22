import sys
sys.stdin = open('input_1974.txt', 'r')

def garo_sero_search(arr):

    for lst in arr: # 배열에서 리스트를 한줄씩 꺼내서
        temp = []
        for i in lst: # 그 리스트에서 한줄씩 꺼내서
            if i not in temp:
                temp.append(i)
            else: # 이미 있다면 그건 중복된 수니까 명백한 False
                return False
    return True

def mini_square_search(arr):
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            # 조그만 네모를 위한 코드
            temp = []
            for k in range(i, i+3):
                for m in range(j, j+3):
                    if arr[k][m] not in temp:
                        temp.append(arr[k][m])
                    else:
                        return False
    return True

def true_or_false(arr1, arr2):
    if garo_sero_search(arr1) and garo_sero_search(arr2) and mini_square_search(arr1):
        return 1
    return 0

TC = int(input())
for test_case in range(1, TC+1):
    N = 9 # 9*9칸 스도쿠
    ARR = [list(map(int,input().split())) for _ in range(N)]
    ARR_axis = list(map(list,zip(*ARR)))

    result = true_or_false(ARR, ARR_axis)

    print('#{} {}'.format(test_case,result))
