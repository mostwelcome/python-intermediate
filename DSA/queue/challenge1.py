'''

Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second.
(hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.


Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order 
thread is consuming the food orders
'''
from collections import deque
import threading
import time


class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        return self.queue.appendleft(item)

    def dequeue(self):
        if self.size() == 0:
            return
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def place_order(self):
        pass

    def server_order(self):
        pass


queue = Queue()


def place_order(order_items):
    for item in order_items:
        queue.enqueue(item)
        print(f'Order placed for: {item}')
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        item = queue.dequeue()
        if item is None:
            print('All order served')
            break
        else:
            print(f'Order served : {item}')
            time.sleep(2)


if __name__ == '__main__':
    order_items = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=place_order, args=(order_items,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()
