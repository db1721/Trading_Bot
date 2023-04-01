from utilities.all_utilities import AllUtilities
from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData
from utilities.database_queries import Database


class Calculations:
    def __init__(self, ticker_symbol=None):
        """
        https://www.omnicalculator.com/finance#s-8
        :param ticker_symbol:
        """
        self.symbol = ticker_symbol
        self.utilities = AllUtilities()

    def benjamin_graham_intrinsic_value(self, earnings_per_share, stock_growth_rate):
        """
        calculate the intrinsic value of stock data provided
        https://www.omnicalculator.com/finance/intrinsic-value
        :param :
        :return:
        """
        try:
            eps = earnings_per_share
            growth_rate = stock_growth_rate
            yield_of_current_bond = 2.57  # Find a way to fetch this

            if eps == 0 or growth_rate == 0:
                raise Exception('An argument is 0')

            intrinsic_value = (eps * (8.5 + (2 * growth_rate)) * 4.4) / yield_of_current_bond
            formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)
            print(f'{self.symbol} Intrinsic Value: {formatted_intrinsic_value}')
        except:
            print(f'{self.symbol} raised an error')

    @staticmethod
    def calculate_total_value_of_portfolio():
        """
        Calculates total value of portfolio
        :return:
        """
        db = Database()
        for key, value in db.get_portfolio().items():
            if len(key) > 0:
                stock_search = SearchForStockData(key)
                print(stock_search.current_price * value['quantity'])


run = Calculations()
run.calculate_total_value_of_portfolio()
