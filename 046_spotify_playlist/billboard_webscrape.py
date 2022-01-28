from bs4 import BeautifulSoup
import requests


def get_songs_from_billboard():
    date = input("What date you want to search TOP100 songs? (YYYY-MM-DD)\n")
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')
    article_tags = soup.select("h3.c-title.a-no-trucate.a-font-primary-bold-s.u-letter-spacing-0021")
    songs = [tag.getText().replace("\n", "") for tag in article_tags]
    return songs, date

