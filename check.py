import pandas as pd

dataset = pd.read_csv('weather_data.csv')

for i in dataset:
    if i['temp'] > 15:
        print(i)
