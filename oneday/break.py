available_candies = 4

x = int(input('How many candies ypu want?'))

i = 1
while i <= x:
    if available_candies < i:
        print('out of stock')
        break
    print('candy')
    i += 1

