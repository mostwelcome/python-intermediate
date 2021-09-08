from collections import deque
class Queue:
    def __init__(self) :
        self.queue = deque()

    def __repr__(self) -> str:
        return ','.join(map(str,self.queue))

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue_size :
            print('Queue is empty')
            return
        return self.queue.pop()

    def queue_size(self):
        return len(self.queue)

queue = Queue()

def decimal_to_binary(num):
    if num > 1:
        decimal_to_binary(num // 2)
    queue.enqueue(num % 2)

decimal_to_binary(12)

print(queue)

# 

# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)

# print(queue.queue)

# queue.dequeue()

# print(queue.queue)
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
'''

# def DecimalToBinary(num):
     
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
 
# # Driver Code
# if __name__ == '__main__':
     
#     # decimal value
#     dec_val = 12
     
#     # Calling function
#     DecimalToBinary(dec_val)


if __name__ == '__main__':
    N = int(input().strip())
    if N%2 == 0:
        if N in range(2,6) or N>20:
            print('Not Weird')
        elif N in range(6,21):
            print('Weird')
    else:
        print('Weird')
