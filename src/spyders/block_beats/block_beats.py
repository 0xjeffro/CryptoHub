import bs4.element
import requests
from bs4 import BeautifulSoup

TAG = "BlockBeats"
BASE_URL = "https://www.theblockbeats.info"


def get_articles():
    all_articles = []
    html = requests.get('https://www.theblockbeats.info/article').text
    bs = BeautifulSoup(html, 'html.parser')

    articles = bs.find_all(name='div', attrs={"class": "home-news"})

    for article in articles:
        title = article.find(name='a').text
        url = article.find(name='a').get('href')
        description = article.find(name='div', attrs={"class": "home-news-lft-content text-ellipsis2"}).text
        # print(title)
        # print(url)
        # print(description)
        if title is not None and url is not None:
            all_articles.append(
                {
                    "title": title,
                    "url": BASE_URL + url,
                    "description": description,
                    "tags": [TAG, "Blockchain"]
                }
            )
    return all_articles
