from utils import rss


def get_articles():
    articles = rss.rss_to_articles('https://www.newsbtc.com/feed/')
    for article in articles:
        article['tags'] = ['NewsBTC', 'Blockchain']
    return articles


if __name__ == '__main__':
    print(get_articles())