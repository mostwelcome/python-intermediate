"""
A
BC
DEF
GHIJ
"""


def print_pattern6(n):
    initial = 'A'
    print(initial)
    for i in range(n):
        for j in range(i):
            initial = chr(ord(initial)+1)
            print(initial, end='')
        print('\n')


print_pattern6(15)
