'''
0 1 1 2 3 5 8 ....
'''

i = int(input())


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


for j in range(i):
    print(fib(j))
