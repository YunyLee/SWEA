import sys
sys.stdin = open('input_5432.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    ARR = list(input())
    # 넣었다 뺐다 반복해줄 스택 생성
    stack = []
    cnt = 0

    for i in range(len(ARR)):
        if ARR[i] == '(':
            stack.append(1)
        elif ARR[i] == ')':
            stack.pop() # 맨뒤에있는 여는괄호를 닫는다.

            if ARR[i-1] == '(': # 레이저라면
                cnt += len(stack) # 스택에 남은 개수만큼 더해준다.
            else:
                cnt += 1 #막대기 하나가 끝난것

    print(f'#{test_case} {cnt}')