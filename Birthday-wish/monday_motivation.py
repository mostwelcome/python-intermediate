import datetime as dt
import random
import smtplib

import requests

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "@blahhh"


def get_quote():
    response = requests.get(url='https://type.fit/api/quotes')
    quotes = response.json()
    monday_motivation_quote = random.choice(quotes)
    print(monday_motivation_quote)
    return monday_motivation_quote


now = dt.datetime.now()

if now.weekday() == 6:
    monday_motivation_quote = get_quote()
    monday_motivation_quote_text = monday_motivation_quote['text']
    monday_motivation_quote_author = monday_motivation_quote['author']
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Monday Motivation\n\n{monday_motivation_quote_text}\n By : {monday_motivation_quote_author}"
        )
