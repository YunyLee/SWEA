import sys
sys.stdin = open('input_5185.txt', 'r')

# 5185 이진수

# 먼저 리스트를 만들어서
sixteen_dict = {
    '0': '0000',
    '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000',
    '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
}

TC = int(input())

for test_case in range(1, TC+1):
    N, SENTENCE = map(str,input().split())
    result = ''

    for i in range(int(N)):
        temp = SENTENCE[i]
        result += sixteen_dict[temp]

    print('#{} {}'.format(test_case, result))

