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

#TODO 1. Create a dictionary in this format:
with open('nato_phonetic_alphabet.csv') as file:
    data = pandas.read_csv(file)

phonetic_dict = {value.letter:value.code for (key,value) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.




def generate_phonetic():
    name = list(input('Enter a name :- '))
    try:
        phonetic_code_words = [phonetic_dict[letter.upper()] for letter in name]
    except:
        print('Sorry,Only letters and alphabet please')
        generate_phonetic()
    else:    
        print(phonetic_code_words)

generate_phonetic()