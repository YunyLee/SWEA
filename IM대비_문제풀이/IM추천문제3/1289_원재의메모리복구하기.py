import sys
sys.stdin = open('input_1289.txt', 'r')

# D3 1289 원재의 메모리 복구하기

def change_switch(lst, idx):
    if lst[idx] == 1:
        lst[idx] = 0
    else:
        lst[idx] = 1

TC = int(input())
for test_case in range(1, TC+1):
    origin_memory = list(map(int,input()))
    reset_memory = [0] * len(origin_memory)
    cnt = 0

    for i in range(len(origin_memory)):
        if (origin_memory[i] == 1 and reset_memory[i] == 0) or (reset_memory[i] == 1 and origin_memory[i] == 0):
            for j in range(i, len(origin_memory)):
                change_switch(reset_memory, j)
            cnt += 1
        if origin_memory == reset_memory:
            break

    print(f'#{test_case} {cnt}')