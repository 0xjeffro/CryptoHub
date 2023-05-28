from push import cubox

from spyders.block_beats import block_beats
import spyders


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    all_articles = []
    all_articles.extend(block_beats.get_articles())
    all_articles.extend(spyders.cmc.news.get_articles())

    cubox.push_to_cubox(all_articles=all_articles)
