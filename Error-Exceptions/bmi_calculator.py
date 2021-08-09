height = float(input('Enter height: '))
weight = float(input('Enter weight: '))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters")
bmi = weight / height ** 2

print(bmi)
