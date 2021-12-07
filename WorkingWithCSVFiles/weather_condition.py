# with open('weather_data.csv') as file:
#     lines = file.readlines()
#     print(lines)

import csv

all_temp = []

with open('../weather_data.csv') as file:
    data = csv.reader(file)
    for row in data:
        if row[1].isnumeric():
            all_temp.append(row[1])

print(all_temp)
