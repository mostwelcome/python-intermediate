with open('file1.txt') as file1:
    list_file1 = file1.readlines()

with open('file2.txt') as file2:
    list_file2 = file2.readlines()

common_list = [int(i) for i in list_file1 if i in list_file2]

print(common_list)
