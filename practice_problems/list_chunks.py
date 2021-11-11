# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 45]
# chunks = 4
# new_list = [a[i:i + chunks] for i in range(0, len(a) - 1, chunks)]
# print(new_list)
#
# addx = lambda x: x + 10
# print(addx(10))
#
# my_list = [(1, 66), (4, 5), (8, 98)]
#
# my_list = sorted(my_list, key=lambda x: x[1])
#
# print(my_list)


def decimalToBinary(ip_val):
    if ip_val >= 1:
        # recursive function call
        decimalToBinary(ip_val // 2)

    # printing remainder from each function call
    print(ip_val % 2, end='')


# Driver Code
if __name__ == '__main__':
    # decimal value
    ip_val = 4

    # Calling special function
    decimalToBinary(ip_val)
