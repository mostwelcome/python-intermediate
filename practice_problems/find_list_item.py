def find_list_item(check):
    for i in range(len(check)):
        for j in range(len(check[i])):
            print(check[i][j])


print(find_list_item([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]))
