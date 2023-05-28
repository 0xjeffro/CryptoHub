import bs4.element
import requests
from bs4 import BeautifulSoup

TAG = "CMC News"
BASE_URL = "https://coinmarketcap.com"


def get_articles():
    all_articles = []
    html = requests.get('https://coinmarketcap.com/headlines/news/').text
    bs = BeautifulSoup(html, 'html.parser')

    articles = bs.find_all(name='div', attrs={"class": "coCmGz"})
    for article in articles:
        title = article.find(name='a').text
        url = article.find(name='a').get('href')
        description = None

        # 若url是本站的相对路径，则跳过
        if url.startswith('/'):
            continue

        if title is not None and url is not None:
            all_articles.append(
                {
                    "title": title,
                    "url": url,
                    "description": description,
                    "tags": [TAG, "Blockchain"]
                }
            )
    return all_articles


if __name__ == '__main__':
    print(get_articles())