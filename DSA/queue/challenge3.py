'''
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.

Solution
'''

from collections import deque

def binary_sequence(num):
    queue = deque()
    queue.append('1')
    for _ in range(num):
        # print(queue)
        element = queue.popleft()
        print(element)
        queue.append(element + '0')
        queue.append(element + '1')
        

binary_sequence(10)