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