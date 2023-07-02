import feedparser
import requests
from urllib.parse import urlparse

#  解析 https://www.newsbtc.com/feed/
req = requests.get('https://www.newsbtc.com/feed/')
feed = feedparser.parse(req.text)


def extract_domain_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + '://' + parsed_url.netloc.split('.')[-2] + '.' + parsed_url.netloc.split('.')[-1]
    return domain


def rss_to_articles(rss_link):
    domain = extract_domain_name(rss_link)
    session = requests.Session()
    req = session.get(domain)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": domain,
    }
    req = session.get(rss_link, headers=headers)
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

