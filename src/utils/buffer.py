from utils.google_sheet import CryptoHubDB
import time


class Buffer:
    def __init__(self):
        self.db = CryptoHubDB()

    def sweep(self, urls, times):  # delete the data 3 days ago
        for t in times:
            if float(t) < time.time() - 60 * 60 * 24 * 3:
                urls[times.index(t)] = ''
                times[times.index(t)] = ''
        # remove empty elements
        urls = [url for url in urls if url != '']
        times = [t for t in times if t != '']

        return urls, times

    def get(self, sweep=True):
        urls, times = self.db.get_all_data()
        if sweep:
            urls, times = self.sweep(urls, times)
        return urls, times

    def set(self, urls, times):
        urls, times = self.sweep(urls, times)
        self.db.set_all_data(urls, times)

    def reset(self, urls, times):
        self.db.clear_all_data()
        urls, times = self.sweep(urls, times)
        self.db.set_all_data(urls, times)

