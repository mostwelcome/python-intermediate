'''
0 1 1 2 3 5 8 ....
'''
i = int(input('Enter number'))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


for j in range(i):
    print(fibo(j))
