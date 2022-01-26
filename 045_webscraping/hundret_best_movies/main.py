import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
web = response.text
soup = BeautifulSoup(web, 'html.parser')
article_tags = soup.find_all(name="h3", class_="title")

movies = [tag.getText() for tag in article_tags][::-1]


with open("movies_list.txt", 'w', encoding='utf-8') as file:
    for movie in movies:
        file.write(movie + "\n")


