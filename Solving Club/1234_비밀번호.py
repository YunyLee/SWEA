import sys
sys.stdin = open('input_1234.txt', 'r')

TC = 10
for test_case in range(1, TC+1):
    N, PW = map(str,input().split())
    stack = []

    for i in PW:
        if len(stack)==0 or i != stack[-1]:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()

    print(f"#{test_case} {''.join(stack)}")