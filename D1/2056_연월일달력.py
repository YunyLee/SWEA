import sys
sys.stdin = open('input_2056.txt', 'r')

TC = int(input())
for test_case in range(1, TC + 1):
    check = False
    DATE = input()
    year = DATE[0:4]
    month = DATE[4:6]
    date = DATE[6:]
    if 1 <= int(month) <= 12:
        if '02' == month:
            if 1 <= int(date) <= 28:
                check = True
        elif '04' == month or '06' == month or '09' == month or '11' == month:
            if 1 <= int(date) <= 30:
                check = True
        else:
            if 1 <= int(date) <= 31:
                check = True

    if check:
        print(f'#{test_case} {year}/{month}/{date}')
    else:
        print(f'#{test_case} {-1}')