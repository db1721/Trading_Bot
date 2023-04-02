from utilities.all_utilities import AllUtilities
from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData


class Calculations:
    def __init__(self, ticker_symbol=None):
        """

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
    def calculate_total_value_of_portfolio(portfolio):
        """
        Calculates total value of portfolio
        :param portfolio:
        :return:
        """
        total_value = 0.0
        for key, value in portfolio.items():
            if len(key) > 0:
                stock_search = SearchForStockData(key)
                temp = stock_search.get_stock_price()
                total_value += float(temp) * float(value['quantity'])

        formatted_total_value = "{:0.2f}".format(total_value)
        print(f'Portfolio Value: ${formatted_total_value}')


# run = Calculations()
# run.calculate_total_value_of_portfolio()
