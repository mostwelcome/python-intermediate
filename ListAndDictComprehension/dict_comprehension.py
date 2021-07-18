import random

names = ['swag', 'tua']
new_dict = {student: random.randint(1, 100) for student in names}

passed_student = {key: value for (key, value) in new_dict.items() if value > 60}
print(new_dict)
print(passed_student)
