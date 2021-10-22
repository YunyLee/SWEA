import sys
sys.stdin = open('input_1242.txt', 'r')

pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}


def find():
    ans = 0
    for i in range(N):  # 세로의길이가 N이라서
        idx = len(arr) - 1  # 마지막 인덱스
        # idx = M * 4 - 1

        while idx >= 55:
            if arr[i][idx] and arr[i - 1][idx] == 0:
                pwd = []
                for _ in range(8):
                    # 뒤에서부터 1 카운트 0카운트 1 카운트를 각각 c4 c3 c2에 저장함.
                    c2 = c3 = c4 = 0
                    # 처음 나오는 0들을 버리자.
                    while arr[i][idx] == 0: idx -= 1
                    while arr[i][idx] == 1: c4, idx = c4 + 1, idx - 1  # 1을 만났으면 1을 카운트
                    while arr[i][idx] == 0: c3, idx = c3 + 1, idx - 1  # 0을 만났으면 카운팅
                    while arr[i][idx] == 1: c2, idx = c2 + 1, idx - 1  # 1을 만났으면 카운팅
                    min_value = min(c2, c3, c4)
                    pwd.append(pattern[(c2 // min_value, c3 // min_value, c4 // min_value)])

                b = pwd[0] + pwd[2] + pwd[4] + pwd[6]  # 짝수번쨰 자리임.
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]

                if (a * 3 + b) % 10 == 0:
                    ans += a + b

            idx -= 1

    return ans


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N 세로의길이, M 가로의길이
    arr = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            arr[i] += hexTobin[tmp[j]]
    # 전부 2진수로 바꿨당~~~

    print("#{} {}".format(tc, find()))



# 다른교수님 코드

# import sys
# sys.stdin = open("암호코드_input.txt")
# hex_to_bin = {
#     '0': [0, 0, 0, 0],
#     '1': [0, 0, 0, 1],
#     '2': [0, 0, 1, 0],
#     '3': [0, 0, 1, 1],
#     '4': [0, 1, 0, 0],
#     '5': [0, 1, 0, 1],
#     '6': [0, 1, 1, 0],
#     '7': [0, 1, 1, 1],
#     '8': [1, 0, 0, 0],
#     '9': [1, 0, 0, 1],
#     'A': [1, 0, 1, 0],
#     'B': [1, 0, 1, 1],
#     'C': [1, 1, 0, 0],
#     'D': [1, 1, 0, 1],
#     'E': [1, 1, 1, 0],
#     'F': [1, 1, 1, 1],
# }
#
# pattern = {
#     (2, 1, 1): 0,
#     (2, 2, 1): 1,
#     (1, 2, 2): 2,
#     (4, 1, 1): 3,
#     (1, 3, 2): 4,
#     (2, 3, 1): 5,
#     (1, 1, 4): 6,
#     (3, 1, 2): 7,
#     (2, 1, 3): 8,
#     (1, 1, 2): 9,
# }
#
#
# def find():
#     ans = 0
#     for i in range(N):  # 행
#         j = M * 4 - 1   # 열
#         while j >= 55:  # j값을 아래 코드에서 변화
#             # 원소의 값이 1이고, 바로 뒤의 값이 0인 경우
#             if arr[i][j] == 1 and arr[i-1][j] == 0:
#                 pwd = []
#                 for k in range(8) : # 암호코드의 수
#                     x = y = z = 0
#                     while arr[i][j] == 1:
#                         z += 1  # 1의 갯수
#                         j -= 1  # 앞으로 앞으로,.....
#                     while arr[i][j] == 0:
#                         y += 1  # 2의 갯수
#                         j -= 1  # 앞으로 앞으로,.....
#                     while arr[i][j] == 1:
#                         x += 1  # 1의 갯수
#                         j -= 1  # 앞으로 앞으로,.....
#                     while arr[i][j] == 0:
#                         j -= 1  # 앞으로 앞으로,.....
#
#                     # 비교해서 암호찾기 -> 뒤쪽암호부터 저장
#                     MIN = min(x, y, z)
#                     pwd.append(pattern[(x//MIN, y//MIN, z//MIN)])
#
#                 odd = pwd[7] + pwd[5] + pwd[3] + pwd[1]
#                 even = pwd[6] + pwd[4] + pwd[2] + pwd[0]
#
#                 # 검증
#                 if (odd * 3 + even) % 10 == 0:
#                     ans += odd + even
#                 # 같은 행에 암호코드 블럭이 겹쳐 있다면 다음 암호블럭에 도착
#                 # j를 오른쪽으로 한칸 이동해야함.
#                 j += 1
#             j -= 1
#     return ans
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     # 16진수 -> 2진수 변환해서 입력받기
#     arr = [[] for _ in range(N)]
#     for i in range(N):
#         tmp = input() # 16진수
#         for j in range(M):
#             arr[i] += hex_to_bin[tmp[j]]
#
#     # for i in arr:
#     #     print(*i)
#
#     print(f'#{tc} {find()}')