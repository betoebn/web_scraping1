from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="storylink")

articles_texts = []
articles_links = []

for article_tag in articles:
    text = article_tag.getText()
    articles_texts.append(text)
    link = article_tag.get("href")
    articles_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(articles_texts)
print(articles_links)
print(article_upvote)

max_value = max(article_upvote)
max_index = article_upvote.index(max_value)

print(articles_texts[max_index])
print(articles_links[max_index])
print(max_value)





































# with open("website.html", encoding="utf8") as data:
#     content = data.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# print(soup.title)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())