def binary_search(numbers_list,find):
    left_index = 0
    right_index = len(numbers_list)-1

    while left_index<= right_index:
        mid_index = (left_index+right_index)//2
        mid_element = numbers_list[mid_index]
        if mid_element == find:
            return mid_index

        elif mid_element > find:
            right_index = mid_index-1
        else:
            left_index = mid_index+1
    return -1


numbers_list = [18,55,66,87,89,90]

find = 999

print(f'Element found at position : {binary_search(numbers_list,find)}')

