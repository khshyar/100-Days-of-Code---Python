# Thanks to Charlie for this code
# https://www.udemy.com/course/100-days-of-code/learn/#questions/19476080

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = []
article_links = []
for article_tag in soup.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])

article_upvotes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

max_points_index = article_upvotes.index(max(article_upvotes))
print(
    f"{article_titles[max_points_index]}, "
    f"{article_upvotes[max_points_index]} points, "
    f"available at: {article_links[max_points_index]}."
)















# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://news.ycombinator.com/news")
# web_page = response.text

# soup = BeautifulSoup(web_page, "html.parser")

# titles = soup.findAll(class_="titleline")
# sublines = soup.findAll(class_="subline")

# data = []

# for i in range(len(titles)-1):
#     description = titles[i].find("a").string
#     link = titles[i].get("href")
#     scores = sublines[i].find(class_="score").string
#     data.append({"title": description, "link": link, "score": int(scores.strip(" points"))})

# maxim = 0
# title = ""
# for i in range(len(data)-1):
#     current_data = data[i]
#     if current_data["score"] > maxim:
#         maxim = current_data["score"]
#         title = f"{current_data['title']}, points = {maxim}, link = {current_data['link']}"
# print(title)