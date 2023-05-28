import pygsheets
import time


class CryptoHubDB:
    def __init__(self):
        self.MAX_ROWS = 800  # max valid rows in the sheet
        self.client = pygsheets.authorize(service_account_env_var='GDRIVE_API_CREDENTIALS')
        self.sh = self.client.open('CryptoHub_DB')
        self.wks = self.sh.sheet1

    def get_all_data(self):
        urls = self.wks.get_col(1, include_tailing_empty=False)
        times = self.wks.get_col(2, include_tailing_empty=False)
        return urls, times

    def clear_all_data(self):
        self.wks.clear(start='A1', end='A{}'.format(self.MAX_ROWS))
        self.wks.clear(start='B1', end='B{}'.format(self.MAX_ROWS))

    def set_all_data(self, data, times):
        self.wks.update_col(1, data[:self.MAX_ROWS])
        self.wks.update_col(2, times[:self.MAX_ROWS])
