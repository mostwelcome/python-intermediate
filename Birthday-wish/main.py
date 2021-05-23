from warnings import simplefilter
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "blahhhh"


'''This is an automatic birthday wish generated mail program'''

# To get todays month and date
today_month = dt.datetime.now().month
today_date = dt.datetime.now().day

today_tuple = (today_month,today_date)

# reading csv file
birthdays_data = pandas.read_csv('birthdays.csv')
birthday_dict = {(data_row['month'],data_row['day']):data_row for (index,data_row) in birthdays_data.iterrows()}

# If today is someones birthday then need to send a mail
if today_tuple in birthday_dict:
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    birthday_person = birthday_dict[today_tuple]['name']
    birthday_person_email = birthday_dict[today_tuple]['email']
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]',birthday_person)
    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=birthday_person_email,
        msg =f"Subject: Happy Birthday\n\n {contents}"
        )
