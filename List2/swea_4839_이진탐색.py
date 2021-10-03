import sys
sys.stdin = open('input_4839.txt', 'r')

# 4839 이진탐색

TC = int(input())

for test_case in range(1, TC+1):
    ALL_PAGES, PAGE_A, PAGE_B = map(int,input().split())
    result = ''
    # 이긴사람이 누군지 알아내기, 비기면 0 출력

    first_page = 1
    last_page = ALL_PAGES
    cnt_a = 0
    cnt_b = 0
    first_a = first_page
    first_b = first_page
    last_a = last_page
    last_b = last_page

    while True:
        mid_a = int((first_a + last_a) / 2)
        if mid_a == PAGE_A:
            break
        if mid_a > PAGE_A:
            last_a = mid_a
            cnt_a += 1
        elif mid_a < PAGE_A:
            first_a = mid_a
            cnt_a += 1

    while True:
        mid_b = int((first_b + last_b) / 2)
        if mid_b == PAGE_B:
            break
        if mid_b > PAGE_B:
            last_b = mid_b
            cnt_b += 1
        elif mid_b < PAGE_B:
            first_b = mid_b
            cnt_b += 1

    if cnt_a < cnt_b:
        result = 'A'
    elif cnt_b < cnt_a:
        result = 'B'
    else:  # cnt_b == cnt_a
        result = '0'

    print('#{} {}'.format(test_case, result))


    # 내가 원래 생각했던 while문
    # while True:
    #     mid_a = int((first_a + last_a) / 2)
    #     mid_b = int((first_b + last_b) / 2)
    #     if mid_a == PAGE_A and mid_b == PAGE_B:
    #         break
    #     if mid_a > PAGE_A:
    #         last_a = mid_a
    #         cnt_a += 1
    #     elif mid_a < PAGE_A:
    #         first_a = mid_a
    #         cnt_a += 1
    #     if mid_b > PAGE_B:
    #         last_b = mid_b
    #         cnt_b += 1
    #     elif mid_b < PAGE_B:
    #         first_b = mid_b
    #         cnt_b += 1
