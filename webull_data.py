import json
from webull import webull # for paper trading, import 'paper_webull'


class WebullData:
    def __init__(self):
        """
        https://pypi.org/project/webull/
        https://github.com/tedchou12/webull

        https://www.youtube.com/watch?v=fqBOePxsCDQ
        https://www.youtube.com/watch?v=3w3ZNQniSbU&t=0s
        """
        self.wb = webull()
        # self.login_to_webull()

        self.email = 'danielbeck783@msn.com'

        # self.wb.get_mfa(self.email)

        results = self.wb.login('danielbeck783@msn.com', 'Millie1721!', 'Python Trading Bot', '161061')
        self.wb.get_trade_token('Millie1721!')
        account = self.wb.get_account()
        print(account)

    def login_to_webull(self):
        """

        :return:
        """
        fh = open('webull_credentials', 'r')
        credential_data = json.load(fh)
        fh.close()

        # print(credential_data)
        self.wb._refresh_token = credential_data['refreshToken']

    def get_all_stocks(self):
        """

        :return:
        """
        print(self.wb.get_history_orders())


web = WebullData()
# web.get_all_stocks()
