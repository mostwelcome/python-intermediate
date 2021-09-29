def is_perfect(n):
    sum_digit = 0
    for i in range(1, n):
        if n % i == 0:
            sum_digit += i

    if sum_digit == n:
        print('Perfect Number')
    else:
        print('Not Perfect')


is_perfect(28)
