n = int(input())
nsum = 0
while n > 0:
    rem = n % 10
    print(rem)
    n = n // 10
    nsum += rem

if nsum % 2 == 0:
    print('Magic even')
else:
    print('Magic odd')

