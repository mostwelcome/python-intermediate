def fibo_number():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = a + c
        yield c


n = 12
f = fibo_number()
for i in range(n):
    print(next(f), end=" ")
