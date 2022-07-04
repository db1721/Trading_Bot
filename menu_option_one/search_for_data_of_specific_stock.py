import yfinance as yf


class SearchForStockData:
    # https: // www.alpharithms.com / python - financial - data - 491110 /
    # https: // towardsdatascience.com / how - to - get - stock - data - using - python - c0de1df17e75
    # https: // pypi.org / project / yfinance /
    def __init__(self, stock_to_search):
        self.ticker_symbol = stock_to_search.upper()

        # print(f'Searching for {self.ticker_symbol}....')

        # get data on this ticker
        self.ticker_data = yf.Ticker(self.ticker_symbol)

        # get the historical prices for this ticker
        ticker_df = self.ticker_data.history(period='1d', start='2010-1-1', end='2020-1-25')

        # see your data
        # print(ticker_df)

        # get stock info
        self.info = self.ticker_data.info

        # get historical market data
        hist = self.ticker_data.history(period="max")

        # show actions (dividends, splits)
        # ticker_data.actions

        # show dividends
        # self.ticker_data.dividends

        # show splits
        # self.ticker_data.splits

        # show financials
        # self.ticker_data.financials
        # self.ticker_data.quarterly_financials

        # show major holders
        # self.ticker_data.major_holders

        # show institutional holders
        # self.ticker_data.institutional_holders

        # show balance sheet
        # self.ticker_data.balance_sheet
        # self.ticker_data.quarterly_balance_sheet

        # show cashflow
        # self.ticker_data.cashflow
        # self.ticker_data.quarterly_cashflow

        # show earnings
        # print(self.ticker_data.earnings)
        # self.ticker_data.quarterly_earnings

        # show sustainability
        # self.ticker_data.sustainability

        # show analysts recommendations
        # self.ticker_data.recommendations

        # show next event (earnings, etc)
        # self.ticker_data.calendar

        # show all earnings dates
        # self.ticker_data.earnings_dates

        # show ISIN code - *experimental*
        # ISIN = International Securities Identification Number
        # self.ticker_data.isin

        # show options expirations
        # self.ticker_data.options

        # show news
        # self.ticker_data.news

        # get option chain for specific expiration
        # opt = self.ticker_data.option_chain('2022-07-15')
        # data available via: opt.calls, opt.puts

    def benjamin_graham_intrinsic_value(self):
        """
        calculate the intrinsic value of stock data provided
        :param stock_info_dict:
        :return:
        """
        try:
            eps = 0
            growth_rate = 0
            yield_of_current_bond = 2.57  # Find a way to fetch this
            for key, value in self.info.items():
                if key == 'trailingEps':
                    # print(f'EPS: {value}')
                    eps = value
                if key == 'sss':
                    # print(f'{key}: {value}')
                    growth_rate = value
                # print(f'{key}: {value}')

            analysis = self.ticker_data.get_analysis(as_dict=True)
            for key, value in analysis.items():
                if key == 'Growth':
                    for key2, value2 in value.items():
                        if key2 == '0Y':
                            # print(f'Growth Rate: {value2}')
                            growth_rate = value2

            if eps is None:
                eps = 0
            if growth_rate is None:
                growth_rate = 0

            intrinsic_value = (eps * (8.5 + (2 * growth_rate)) * 4.4) / yield_of_current_bond
            formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)
            print(f'{self.ticker_symbol} Intrinsic Value: {formatted_intrinsic_value}')
        except:
            print(f'{self.ticker_symbol} raised an error')


if __name__ == '__main__':
    run = SearchForStockData('orc')
    run.benjamin_graham_intrinsic_value()
