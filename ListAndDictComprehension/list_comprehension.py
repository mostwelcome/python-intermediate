item = [1, 2, 3, 4, 5]
new_list = [i + 1 for i in item]

print(new_list)

name = "Swagata"
new_list_name = [letter for letter in name]
print(new_list_name)

double_list = [i * 2 for i in range(1, 5)]
print(double_list)

names_list = ['swag', 'Tua']

filtered_names_list = [name.upper() for name in names_list if len(name) > 3]

print(filtered_names_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squaring number
squared_numbers = [number ** 2 for number in numbers]
print(squared_numbers)

# check for even numbers

even_numbers = [number for number in numbers if (number % 2) == 0]
print(even_numbers)
