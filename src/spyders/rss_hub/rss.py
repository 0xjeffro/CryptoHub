from utils.rss import rss_to_articles
source = [
    {
        'name': 'BlockBeats',
        'url': 'https://api.theblockbeats.news/v1/open-api/home-xml',
    },
    {
        'name': 'NewsBTC',
        'url': 'https://www.newsbtc.com/feed/',
    },
    {
        'name': 'NewOrderDAO',
        'url': 'https://medium.com/feed/neworderdao',
    },
    {
        'name': 'IC3',
        'url': 'https://medium.com/feed/initc3org',
    },
]


def get_articles():
    all_articles = []
    for rss in source:
        articles = rss_to_articles(rss['url'])
        for article in articles:
            article['tags'] = [rss['name'], ]
        all_articles.extend(articles)
    return all_articles


if __name__ == '__main__':
    articles = get_articles()
    print(articles)
    print(len(articles))

