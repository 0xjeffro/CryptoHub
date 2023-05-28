import requests
from bs4 import BeautifulSoup

TAG = "Followin News"
BASE_URL = "https://followin.io"


def get_articles():
    all_articles = []
    html = requests.get('https://followin.io/zh-Hans/news').text
    bs = BeautifulSoup(html, 'html.parser')

    articles = bs.find_all(name='a', attrs={"target": "_self"})
    for article in articles:
        title = article.text
        url = article.get('href')
        description = None
        # 补全url
        if url.startswith('/'):
            url = BASE_URL + url

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
