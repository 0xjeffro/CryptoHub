from utils.rss import rss_to_articles
source = [
    'https://api.theblockbeats.news/v1/open-api/home-xml',
    'https://www.newsbtc.com/feed/',
    'https://medium.com/feed/neworderdao',
    'https://medium.com/feed/initc3org',
    'https://medium.com/feed/ethereum-push-notification-service',
]


def get_articles():
    all_articles = []
    for rss_link in source:
        print(rss_link)
        articles = rss_to_articles(rss_link)
        all_articles.extend(articles)
    return all_articles


if __name__ == '__main__':
    articles = get_articles()
    print(articles)
    print(len(articles))

