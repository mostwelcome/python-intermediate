# open_list = ['{', '[', '(']
# close_list = ['}', ']', ')']
#
#
# def check_balanced(s):
#     stack = []
#     for i in s:
#         if i in open_list:
#             stack.append(i)
#         elif i in close_list:
#             p = close_list.index(i)
#             if (len(stack) > 0) and open_list[p] == stack[len(stack) - 1]:
#                 stack.pop()
#             else:
#                 return 'Not valid'
#     if len(stack) == 0:
#         return 'valid'
#     else:
#         return 'Not valid'
#
#
# s = '{[((}))'
#
# check_balanced(s)
#
# def exception_handler(func):
#     def wrapper():
#         try:
#             func()
#         except Exception:
#             print('Exception')
#
#
# @exception_handler
# def divide_numbers(a, b):
#     return a / b
#
#
# divide_numbers(10, 0)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} : {self.age}'


p1 = Person('abc', 20)
p2 = Person('xyz', 30)
p3 = Person('tuv', 15)
l = [p1, p2, p3]

l.sort(key=lambda x: x.age, reverse=True)

print(l)
