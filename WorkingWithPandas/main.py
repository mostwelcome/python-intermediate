import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print('only temp data\n')
# print(type(data))
# print(type(data['temp']))

print(data.to_dict())

temp_series = data['temp']

print(data.temp)

temp_list = temp_series.to_list()
print(temp_list)

print('calculating avg temp')
avg = sum(temp_list) / len(temp_list)
print(f'avg is {avg}')

# 2nd way

print(temp_series.mean())

print(f'max temp is :{temp_series.max()}')

# get data row
print('get the row of a dataframe')
print(data[data.day == 'Monday'])

# get the row where the temp is max

print('max temp row is : ')
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

cel = int(monday.temp)
temp_f = cel * 9 / 5 + 32
print(f'temp in farenheit : - {temp_f}')

# create a dataframe
data_dict = {
    'students_name': ['swagata', 'Tua'],
    'score': ['90', '80']
}

created_data = pandas.DataFrame(data_dict)
print(created_data)

# to create a new csv file from the dataframe
created_data.to_csv('new_data.csv')
