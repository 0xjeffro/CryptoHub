import feedparser
import requests

#  解析 https://www.newsbtc.com/feed/
req = requests.get('https://www.newsbtc.com/feed/')
feed = feedparser.parse(req.text)


def rss_to_articles(rss_link):
    req = requests.get(rss_link)
    feed = feedparser.parse(req.text)
    articles = []
    for entry in feed.entries:
        title = entry.title
        url = entry.link

        if title is not None and url is not None:
            articles.append(
                {
                    "title": title,
                    "url": url,
                    "description": None,
                }
            )
    return articles


if __name__ == '__main__':
    print(rss_to_articles('https://www.newsbtc.com/feed/'))

