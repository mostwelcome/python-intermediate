'''
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]"

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True

'''

from collections import deque

open_list = ['{', '(', '[']
close_list = ['}', ')', ']']

match_dict = {
    ')': '(',
    ']': '[',
    '}': '{'
}


class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        if item in open_list or item in close_list:
            return self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_match(self, ch1, ch2):
        return match_dict[ch1] == ch2

    def is_balanced(self, text):
        for ch in text:
            if ch in open_list:
                self.push(ch)
            if ch in close_list:
                if self.size() == 0:
                    return False
                if not self.is_match(ch, stack.pop()):
                    return False

        return stack.size() == 0


stack = Stack()

 
print(stack.is_balanced("({a+b})"))
print(stack.is_balanced("))((a+b}{"))
print(stack.is_balanced("((a+b))"))
print(stack.is_balanced("))") )
print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))