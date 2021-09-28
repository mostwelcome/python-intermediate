"""
#
##
###
####
#####
"""


def print_pattern2(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('#', end='')
        print('\n')


print_pattern2(9)
