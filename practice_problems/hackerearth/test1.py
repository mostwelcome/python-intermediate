# # # # # mylist = [1,2,3,4]
# # # # # print('a'.join((str(item) for item in mylist)))
# # # #
# # # #
# # # # a = ' Hello World\n'
# # # # print(a.strip())
# # #
# # # a = [7, 3, 22, 42, 6]
# # # print(a.sort(reverse=True))
# # # print(a[1])
# #
# # mylist = ['navin', 3, 7, 'navin', 3]
# #
# # print(len(set(mylist)))
#
# mylist = [1, 3, 5, 15, 22, 'b']
# print(sum([i for i in mylist if isinstance(i, int) and i % 2 == 0]))

# with open('input.txt') as i:
#     mylist = [k.strip() for k in i.readlines()]
#     print(mylist)
#     filtered_list = []
#     for element in mylist:
#         try:
#             j = int(element)
#             if j % 2 != 0:
#                 filtered_list.append(j)
#         except ValueError:
#             break
#     # filtered_list = [i for int(i) in mylist if i % 2 == 0]
#
# print('\n'.join(str(ele) for ele in filtered_list))
# with open('input.txt') as i:
#     mylist = [k.strip() for k in i.readlines()]
#     filtered_list = []
#     for element in mylist:
#         try:
#             j = int(element)
#             if j % 2 != 0:
#                 filtered_list.append(j)
#         except ValueError:
#             break
#
# print('\n'.join(str(ele) for ele in filtered_list[:4]))

# list1 = [[1, 2, 3, 4], [2, 4, 5], [[0, 0], [1, 1]]]
# list2 = list1[0]
# list3 = list1[2][0]
# list3[0] = 10
# a = list1[0][3]
# a = 10
# print(list2)
# list2[1] = 5
# print(list1)

# class Abc:
#     def __init__(self):
#         self.variable = 'old'
#         self.change(self.variable)
#
#     def change(self, var):
#         var = 'new'
#
#
# a = Abc()
# print(a.variable)
