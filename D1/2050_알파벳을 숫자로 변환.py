import sys
sys.stdin = open('input_2050.txt', 'r')

ALPHABET = input()

for i in ALPHABET:
    print(ord(i) - 64, end=' ')