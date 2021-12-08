import sys


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


# Function to calculate how many numbers
# from 1 to num are divisible by a or b
def divTermCount(a, b, lcm, num):
    # calculate number of terms divisible
    # by a and by b then, remove the terms
    # which are divisible by both a and b
    return (num // a + num // b) - (num // lcm)


# Binary search to find the nth term
# divisible by a or b
def findNthTerm(a, b, n):
    # set low to 1 and high to max(a, b)*n,
    # here we have taken high as 10^18
    low = 1;
    high = sys.maxsize
    lcm = (a * b) // gcd(a, b)
    while low < high:
        mid = low + (high - low) // 2

        # if the current term is less
        # than n then we need to increase
        # low to mid + 1
        if divTermCount(a, b, lcm, mid) < n:
            low = mid + 1

        # if current term is greater
        # than equal to n then high = mid
        else:
            high = mid
    return low


test_cases = int(input())

for i in range(test_cases):
    a, b, n = input().split(' ')
    print(findNthTerm(int(a), int(b), int(n)))
