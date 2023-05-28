import json
import os
import time

from spyders import block_beats
import requests

from utils import buffer


def push_to_cubox(api=None, all_articles=None):
    if api is None:
        api = os.getenv("CUBOX_API")
        print("CUBOX_API: {}".format(api))

    buf = buffer.Buffer()
    urls, times = buf.get(sweep=True)
    new_articles = []
    for article in all_articles:
        if article["url"] not in urls:
            new_articles.append(article)

    for article in new_articles:
        data = {
            "type": "url",
            "content": article["url"],
            "title": article["title"],
            "description": article["description"],
            "tags": article["tags"],
            "folder": "Crypto"
        }

        # Cubox DOC: https://help.cubox.pro/save/89d3/
        req = requests.post(api, json=data)

        if json.loads(req.text)["code"] != 200:
            print("Cubox push failed, url: {}, message: {}".format(
                article["url"],
                json.loads(req.text)["message"]))
        else:
            print("Cubox push success!")
            urls.insert(0, article["url"])
            times.insert(0, str(time.time()))

    buf.reset(urls, times)
