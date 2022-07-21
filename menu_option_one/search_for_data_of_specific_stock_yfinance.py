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
        # ticker_df = self.ticker_data.history(period='1d', start='2010-1-1', end='2020-1-25')

        # see your data
        # print(ticker_df)

        # get stock info
        self.info = self.ticker_data.info

        # get historical market data
        # hist = self.ticker_data.history(period="max")

        # show actions (dividends, splits)
        # ticker_data.actions

        # show dividends
        # print(self.ticker_data.dividends)

        # show splits
        # self.ticker_data.splits

        # show financials
        # print(self.ticker_data.financials)
        # print(self.ticker_data.quarterly_financials)

        # show major holders
        # self.ticker_data.major_holders

        # show institutional holders
        # self.ticker_data.institutional_holders

        # show balance sheet
        # print(self.ticker_data.balance_sheet)
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
            current_price = 0
            margin_of_safety = .65
            buy_or_sell = ''
            value_difference = 0
            yield_of_current_bond = 3.8  # Find a way to fetch this
            iv_dict = {}

            # Get stock price
            for key, value in self.info.items():
                # print(f'{key}: {value}')
                if key == 'currentPrice' and str(value) != 'None':
                    # print(f'Current Price: {value}')
                    current_price = value
                    break

            try:
                # Get EPS
                for key, value in self.info.items():
                    # print(f'{key}: {value}')
                    if key == 'forwardEps' and str(value) != 'None':
                        # print(f'EPS (Forward): {value}')
                        eps = value
                        break
                    if key == 'trailingEps':
                        # print(f'EPS (Trailing): {value}')
                        eps = value
                        break
            except:
                pass

            # financials = self.ticker_data.financials
            # for key, value in financials.items():
            #     print(f'{key}: {value}')

            try:
                # Get growth
                analysis = self.ticker_data.get_analysis(as_dict=True)
                for key, value in analysis.items():
                    # print(f'{key}: {value}')
                    if key == 'Growth':
                        for key2, value2 in value.items():
                            if key2 == '0Q' and str(value2) != 'nan' and str(value2) != 'None':
                                # print(f'Growth Rate (0Q): {value2}')
                                growth_rate = value2
                                break
                            elif key2 == '+1Q' and str(value2) != 'nan' and str(value2) != 'None':
                                # print(f'Growth Rate (+1Q): {value2}')
                                growth_rate = value2
                                break
                            elif key2 == '0Y' and str(value2) != 'nan' and str(value2) != 'None':
                                # print(f'Growth Rate (0Y): {value2}')
                                growth_rate = value2
                                break
                            elif key2 == '+1Y' and str(value2) != 'nan' and str(value2) != 'None':
                                # print(f'Growth Rate (+1Y): {value2}')
                                growth_rate = value2
                                break
                            elif key2 == '+5Y' and str(value2) != 'nan' and str(value2) != 'None':
                                # print(f'Growth Rate (+5Y): {value2}')
                                growth_rate = value2
                                break
            except:
                pass

            try:
                # Another check for growth
                if growth_rate == 0:
                    for key, value in self.info.items():
                        if key == 'revenueGrowth' and str(value) != 'nan' and str(value) != 'None':
                            # print(f'Growth Rate (Revenue): {value}')
                            growth_rate = value
            except:
                pass

            # Force to break it if data not found
            if eps == 0:
                eps = None
            if growth_rate == 0:
                growth_rate = None

            # # Calculate Intrinsic Value (Original)
            # intrinsic_value = (eps * (8.5 + (2 * growth_rate)) * 4.4) / yield_of_current_bond
            # formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)

            # Calculate Intrinsic Value (Revised)
            intrinsic_value = (eps * (7 + growth_rate) * 4.4) / yield_of_current_bond
            formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)

            # Calculate value difference
            value_difference = current_price / intrinsic_value
            value_difference = value_difference * 100
            formatted_value_difference = "{:0.2f}".format(value_difference)

            # Acceptable buy price
            acceptable_buy_price = margin_of_safety * intrinsic_value
            formatted_acceptable_buy_price = "{:0.2f}".format(acceptable_buy_price)

            # print(f'{self.ticker_symbol} Intrinsic Value ${formatted_intrinsic_value} at '
            #       f'${formatted_acceptable_buy_price} at a value of {formatted_value_difference}%')
            try:
                iv_dict.update({self.ticker_symbol: f'{formatted_value_difference}% @ ${formatted_acceptable_buy_price} '
                                                    f'for a rebate of ${current_price-formatted_acceptable_buy_price}'})
                return iv_dict
            except:
                pass
        except:
            # print(f'{self.ticker_symbol} does not have Intrinsic Value')
            pass

    def print_stock_info(self):
        """

        :return:
        """
        for key, value in self.info.items():
            # if key == 'trailingEps':
            print(f'{key}: {value}')


if __name__ == '__main__':
    run = SearchForStockData('iep')
    # run.print_stock_info()
