def get_prime_factors(n):
    list_prime_factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            list_prime_factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return list_prime_factors


print(get_prime_factors(13))
