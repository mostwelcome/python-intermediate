from bs4.builder import HTML
import requests
from bs4 import  BeautifulSoup

date = input('Which year do u want to travel too? Type the date in this format YYYY-MM-DD: ')

URL = "https://www.billboard.com/charts/hot-100/"+date

response = requests.get(url=URL)

response.raise_for_status

with open('./Beautiful_soup/Top-100-songs-on-historical-day/response.txt','w', encoding='utf-8') as file:
    file.write(response.text)


soup = BeautifulSoup(response.text,"html.parser")

songs_name_span = soup.find_all(name='span',class_="chart-element__information__song text--truncate color--primary")

songs_rank_span = soup.find_all(name='span' , class_="chart-element__rank__number")

songs_list = [songs.getText() for songs in songs_name_span]
songs_rank = [songs.getText() for songs in songs_rank_span]

print(songs_list)
print(songs_rank)

with open('./Beautiful_soup/Top-100-songs-on-historical-day/best_songs_list.txt','a') as f:
    for i in range(0,100):
        f.write(songs_rank[i]+" -- "+songs_list[i] + "\n")
