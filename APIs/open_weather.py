# Authenticates through API key
from tkinter.constants import TRUE

import requests
from twilio.rest import Client

API_KEY = ""
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

parameters = {
    'lat': 17.781070,
    'lon': 121.565450,
    'appid': API_KEY,
    'exclude': 'currently,minutely,daily'
}
response = requests.get(url="http://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data['hourly'][0]['weather'][0]['id'])

ids = [id['weather'][0]['id'] for id in weather_data['hourly']]
first_twelve_values = ids[:12]

will_rain = False
for value in first_twelve_values:
    if value < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body="You need your umbrella today ☂️!",
            from_='+18302641656',
            to='+91 98306 96471'
        )
        print(message.sid)
        will_rain = TRUE
        break
if not will_rain:
    print('you are safe')

print(first_twelve_values)
