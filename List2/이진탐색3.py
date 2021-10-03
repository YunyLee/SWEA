import sys
sys.stdin = open('input_4839.txt', 'r')

# 4839 이진탐색

TC = int(input())

for test_case in range(1, TC+1):
    ALL_PAGES, PAGE_A, PAGE_B = map(int,input().split())
    result = '0'
    # 이긴사람이 누군지 알아내기, 비기면 0 출력

    first_a = first_b = 1
    last_a = last_b = ALL_PAGES

    while True:
        mid_a = int((first_a + last_a) / 2)
        mid_b = int((first_b + last_b) / 2)
        if mid_b == PAGE_B and mid_a == PAGE_A:
            break
        if mid_a == PAGE_A and mid_b != PAGE_B:
            result = 'A'
            break
        elif mid_b == PAGE_B and mid_b != PAGE_A:
            result = 'B'
            break
        if mid_a > PAGE_A:
            last_a = mid_a
        elif mid_a < PAGE_A:
            first_a = mid_a
        if mid_b > PAGE_B:
            last_b = mid_b
        elif mid_b < PAGE_B:
            first_b = mid_b

    print('#{} {}'.format(test_case, result))