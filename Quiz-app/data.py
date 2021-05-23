import requests

paramaters = {
    'amount':10,
    'type':'boolean'
}

response = requests.get(url="https://opentdb.com/api.php",params=paramaters)
response.raise_for_status

results = response.json()['results']