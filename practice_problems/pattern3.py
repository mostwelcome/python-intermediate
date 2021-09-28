"""
0
01
012
0123
01234
012345
"""


def print_pattern3(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(j, end='')
        print('\n')


print_pattern3(9)
