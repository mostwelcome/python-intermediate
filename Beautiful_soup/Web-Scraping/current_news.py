import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get('href')
    article_links.append(link)

article_upvote = [int(upvote.getText().split(" ")[0]) for upvote in soup.find_all(name='span', class_='score')]
# print(article_texts)
# print('\n')
# print(article_links)
# print('\n')
print(article_upvote)

max_upvote = article_upvote.index(max(article_upvote))
max_upvote_text = article_texts[max_upvote]
max_upvote_link = article_links[max_upvote]

print(max_upvote, max_upvote_text, max_upvote_link)
