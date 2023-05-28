from utils import rss


def get_articles():
    articles = rss.rss_to_articles('https://rss.panewslab.com/zh/gtimg/rss')
    for article in articles:
        article['tags'] = ['PanNews', 'Blockchain']
    return articles


if __name__ == '__main__':
    print(get_articles())