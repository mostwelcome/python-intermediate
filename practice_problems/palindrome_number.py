def check_palindrome(n):
    bkp = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    if rev == bkp:
        print('Palindrome')
    else:
        print('Not Palindrome')


check_palindrome(565)
