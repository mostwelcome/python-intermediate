student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
with open('nato_phonetic_alphabet.csv') as file:
    data = pandas.read_csv(file)
    print(type(data))
    print(data.letter)

phonetic_dict = {value.letter:value.code for (key,value) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = list(input('Enter a name :- '))
phonetic_code_words = [phonetic_dict[letter.upper()] for letter in name]

print(phonetic_code_words)