from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData
from utilities.database_queries import Database


class AddStock:
    def __init__(self):
        """
        Functions for adding stock to portfolio
        """
        self._portfolio_query = Database()
        self._portfolio_dictionary = self._portfolio_query.get_portfolio()

    def add_stock(self):
        """
        Add a stock to portfolio
        :return:
        """
        print(f'Trading Bot - Add Stock')
        while True:
            user_input = input(
                'Enter Stock to Add: '
            )
            if user_input.upper() in self._portfolio_dictionary.keys():
                print(f'{user_input.upper()} already on portfolio')
                break
            else:
                try:
                    stock_data = SearchForStockData(user_input.upper())
                    if str(stock_data.current_price).isnumeric():
                        self._get_added_stock_portfolio_weight(user_input.upper())
                    print(f'{user_input.upper()} added to Portfolio')
                    break
                # Checks if the stock exists
                except TypeError:
                    print(f'Unable to add {user_input.upper()} to Portfolio')

    def _get_added_stock_portfolio_weight(self, stock_adding):
        """
        Gets portfolio weight from user
        :return:
        """
        while True:
            user_input = input(
                f"Enter Portfolio Weight for {stock_adding}. Enter '' to auto balance: "
            )
            if user_input in self._portfolio_dictionary.keys():
                print(f'{user_input.upper()} already on portfolio')
                break
            else:
                pass

