import sys
sys.stdin = open('input_4839.txt', 'r')

# 4839 이진탐색

def binary_search(last_page, page):
    cnt = 0
    first_page = 1
    while True:
        mid = int((first_page + last_page) / 2)
        if mid == page:
            return cnt
        if mid > page:
            last_page = mid
            cnt += 1
        elif mid < page:
            first_page = mid
            cnt += 1

TC = int(input())

for test_case in range(1, TC+1):
    ALL_PAGES, PAGE_A, PAGE_B = map(int,input().split())
    result = ''
    # 이긴사람이 누군지 알아내기, 비기면 0 출력

    cnt_a = cnt_b = 0

    cnt_a = binary_search(ALL_PAGES, PAGE_A)
    cnt_b = binary_search(ALL_PAGES, PAGE_B)

    print(cnt_a)
    print(cnt_b)

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_b < cnt_a:
        result = 'B'
    else:  # cnt_b == cnt_a
        result = '0'

    print('#{} {}'.format(test_case, result))