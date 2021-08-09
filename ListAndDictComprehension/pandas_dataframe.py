import pandas

student_dict = {
    'student': ['swag', 'tua'],
    'scores': [99, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)
