def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def is_strongnumber(n):
    sum_digit = 0
    temp = n
    while n > 0:
        rem = n % 10
        sum_digit += factorial(rem)
        n = n//10

    if temp == sum_digit:
        print('Strong Number')
    else:
        print('Not Strong Number')


is_strongnumber(145)
