"""
A
BB
CCC
DDDD
EEEEE
"""


def print_pattern5(n):
    for i in range(1, n + 1):
        initial = chr(ord('A') + i-1)
        for j in range(i):
            print(initial, end='')
        print('\n')


print_pattern5(5)
