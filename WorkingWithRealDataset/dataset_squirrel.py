import pandas
data = pandas.read_csv('SquirrelCensusSquirrel.csv')
print(data['Primary Fur Color'])

gray_squirrel = data[data['Primary Fur Color'] == 'Gray']
cinnamon_squirrel = data[data['Primary Fur Color'] == 'Cinnamon']
black_squirrel = data[data['Primary Fur Color'] == 'Black']

squirrel_dict = {
    'squirrel_color':['gray_squirrel','cinnamon_squirrel','black_squirrel'],
    'count': [len(gray_squirrel),len(cinnamon_squirrel),len(black_squirrel)]
}

squirrel_dataframe = pandas.DataFrame(squirrel_dict)

#saving the final result to csv
squirrel_dataframe.to_csv('squirrel_count.csv')