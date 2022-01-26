from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/front")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
article_tag = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for tag in article_tag:
    article_texts.append(tag.getText())
    article_links.append(tag.get("href"))

article_upvotes = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

largest_index = article_upvotes.index(max(article_upvotes))
print(article_texts[largest_index])









# ------------------------------- examples of use------------------------- #
# with open("website.html", "r") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
#
# # print(soup.p)
# # print(soup.find_all(name="a"))
# # all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading.string)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)
