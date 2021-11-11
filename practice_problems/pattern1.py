"""
1
22
333
4444
55555
"""

# def print_pattern1(n):
#     for i in range(n+1):
#         for j in range(i):
#             print(i, end="")
#         print("\n")
#
#
# print_pattern1(8)


'''
0
0 1
0 1 2
0 1 2 3
'''


def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print(j, end=" ")
        print("\n")


pattern2(5)
