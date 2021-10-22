import sys
sys.stdin = open('input_4408.txt', 'r')

# TC = int(input())
# for test_case in range(1, TC+1):
#     N = int(input()) # 학생수
#     # 방번호가 최대 400이므로 복도의 번호는 최대 200이다. 따라서 카운트할 리스트 200개로 초기화
#     bokdo = [0] * 200
#     for i in range(N): # 학생수
#         START, END = map(int,input().split()) # 시작방과 끝방
#         # 작은수를 스타트로 확실히 해주기
#         if START > END:
#             START, END = END, START
#         bokdo_start = 0
#         bokdo_end = 0
#         if START % 2: # 홀수면
#             bokdo_start = START//2
#         else: # 짝수면
#             bokdo_start = (START+1)//2
#         if END % 2: # 홀수면
#             bokdo_end = END//2
#         else: # 짝수면
#             bokdo_end = (END-1)//2
#         for j in range(bokdo_start, bokdo_end+1):
#             bokdo[j] += 1
#
#     print('#{} {}'.format(test_case,max(bokdo)))

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input()) # 학생수
    # 방번호가 최대 400이므로 복도의 번호는 최대 200이다. 따라서 카운트할 리스트 200개로 초기화
    bokdo = [0] * 201
    for i in range(N): # 학생수
        START, END = map(int,input().split()) # 시작방과 끝방
        # 작은수를 스타트로 확실히 해주기
        if START > END:
            START, END = END, START
        START = (START+1)//2
        END = (END+1)//2
        for j in range(START, END+1):
            bokdo[j] += 1

    print('#{} {}'.format(test_case,max(bokdo)))