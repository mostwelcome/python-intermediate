def is_armstrong(n):
    temp = n
    digit_sum = 0
    while n > 0:
        rem = n % 10
        n = n//10
        digit_sum += rem ** 3

    if digit_sum == temp:
        print('It is Armstrong number')
    else:
        print('Not Armstrong')


is_armstrong(25)
