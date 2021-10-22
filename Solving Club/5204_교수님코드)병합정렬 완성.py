from collections import deque


# 두개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)

    # 두 부분집합이 모두 존재할 때
    while left and right:
        # 왼쪽이 작을 때
        if left[0] <= right[0]:
            result.append(left.popleft())
        # 오른쪽이 작을 때
        else:
            result.append(right.popleft())
    # 왼쪽만 남아 있으면
    if left:
        result.extend(left)
    # 오른쪽만 남아 있으면
    if right:
        result.extend(right)

    return result


def merge_sort(arr):
    global cnt
    # arr를 반씩 나누어서 하나 남을때 까지 나누기
    if len(arr) == 1:  # 하나 남을때
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1

    # 합치기
    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N // 2], cnt))