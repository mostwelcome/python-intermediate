"""
1
22
333
4444
55555
"""


def print_pattern1(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end='')
        print('\n')


print_pattern1(9)
