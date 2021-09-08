'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''

# num = int(input('Enter a number : '))

# odd_numbers = [i for i in range(1,num+1) if i %2!=0]
# print(odd_numbers)

n = int(input().strip())
binary_number = bin(n)[2:]
# count = max((binary_number.split('0')).count('1'))
print(binary_number)
count = max(binary_number.split('0')).count('1')
print(count)  