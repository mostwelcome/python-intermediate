# File not found
# with open('a.txt') as file:
#     file.read()

try:
    file = open('a.txt')
    my_dict = {'key': 'value'}
    value = my_dict["key"]
except FileNotFoundError:
    print('There was an error')
    open('a.txt', 'w')
except KeyError as error_message:
    print(f'The key {error_message} does not exist')
    my_dict["doesn't exist"] = 'somevalue'
    print(my_dict)
else:
    content = file.read()
    print(content)
finally:
    print('file is closed')
    file.close()
    # to raise an exception
    # raise FileNotFoundError("I made up this")

# KeyError:

# my_dict = {'key':'value'}
# value = my_dict["doesn't exist"]

# Index error:IndexError: list index out of range
# my_list[4]

# Type error:TypeError: can only concatenate str (not "int") to str

# text = 'abc'
# print(text+5)
