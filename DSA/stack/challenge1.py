'''
Write a function in python that can reverse a string using stack data structure.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
'''
from collections import deque


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        return self.stack.append(item)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return ''

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def reverse_string(self, text):
        reversed_string = ''
        for char in text:
            self.push(char)
        while self.size() > 0:
            reversed_string += self.pop()
        return reversed_string


stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.stack)

# stack.pop()
# print(stack.stack)
# print(stack.peek())

reversed_string = stack.reverse_string("We will conquere COVID-19")
print(reversed_string)
