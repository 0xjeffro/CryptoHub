from push import cubox

from spyders.block_beats import block_beats
from spyders.cmc import news as cmc_news
from spyders.followin import news as followin_news

from spyders.newsbtc import rss as newsbtc_rss
from spyders.pannews import rss as pannews_rss

from spyders.rss_hub import rss as rss_hub_rss


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_articles = []
    # all_articles.extend(block_beats.get_articles())
    all_articles.extend(cmc_news.get_articles()[:5])
    # all_articles.extend(followin_news.get_articles())
    #all_articles.extend(newsbtc_rss.get_articles())
    #all_articles.extend(pannews_rss.get_articles())
    all_articles.extend(rss_hub_rss.get_articles())

    # shuffle the articles
    import random
    random.shuffle(all_articles)

    # print(len(all_articles))

    cubox.push_to_cubox(all_articles=all_articles)
