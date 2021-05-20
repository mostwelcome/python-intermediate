import requests

from datetime import datetime
MY_LAT = 22.595770
MY_LNG = 88.263641

parameters = {
    'lat':MY_LAT,
    'lng':MY_LNG,
    'formatted': 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()

data = response.json()

time_now = datetime.now()

print(f"Sunrise time: {data['results']['sunrise'].split('T')[1].split(':')[0]}")
print(f"Sumset time: {data['results']['sunset'].split('T')[1].split(':')[0]}")
print(time_now.hour)
