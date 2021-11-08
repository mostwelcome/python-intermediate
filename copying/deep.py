import copy

# This is only works for single level
# for multiple level need to do copy.deepcopy()
# works for custom copy as well
my_list = [1, 2, 3, 4, 5, 6]
new_list = copy.copy(my_list)
new_list[1] = 100

print("original ", my_list)
