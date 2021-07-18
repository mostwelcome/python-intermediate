from bs4 import BeautifulSoup

with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.prettify())

# give first occurrence
print(soup.a)

all_paragraphs = soup.find_all(name='p')
print(all_paragraphs)
