import yfinance as yf


class SearchForStockData:
    # https: // www.alpharithms.com / python - financial - data - 491110 /
    # https: // towardsdatascience.com / how - to - get - stock - data - using - python - c0de1df17e75
    # https: // pypi.org / project / yfinance /
    def __init__(self, stock_to_search):
        self.ticker_symbol = stock_to_search.upper()

        # Variables
        self.eps = 0
        self.growth_rate = 0
        self.current_price = 0
        self.margin_of_safety = .65
        self.value_difference = 0
        self.aggregate_total = 0.0

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
        :return:
        """
        try:
            self._do_the_thing(self.ticker_symbol)
        except:
            try:
                # Get stock price
                holding_dict = {}
                for key, value in self.info.items():
                    # print(f'{key}: {value}')
                    if key == 'holdings':
                        # print(f'{key}: {value}')
                        for i in value:
                            symbol = ''
                            holding_percentage = 0.00
                            for key2, value2 in i.items():
                                if key2 == 'symbol' and str(value2) != 'None' and str(value2) != 'nan' and str(value2) != '':
                                    # print(f'Symbol: {value2}')
                                    symbol = value2
                                if key2 == 'holdingPercent' and str(value2) != 'None' and str(value2) != 'nan':
                                    # print(f'Holding Percentage: {value2}')
                                    holding_percentage = value2
                                if symbol != '' and holding_percentage > 0:
                                    holding_dict.update({symbol: holding_percentage})

                print(self.ticker_symbol)
                total_weight = 0.0
                self.aggregate_total = 0.0
                for stock, percent in holding_dict.items():
                    # print(f'    {stock}: {percent*100}')
                    total_weight += percent*100
                    self._do_the_thing(stock.strip(), callout=False)

                # intrinsic_value_data = self._calculate_intrinsic_value(self.aggregate_total)

                # print(f'    Total Percentage: {total_weight}')
                print(f'    Aggregate Intrinsic Value: {self.aggregate_total}')

                # if self.aggregate_total != 0:
                #     print(self.aggregate_total)
            except:
                print(f'{self.ticker_symbol} does not have Intrinsic Value')
                pass

    def _do_the_thing(self, ticker, callout=True):
        """

        :return:
        """
        # Get new stocks ticker data
        self.ticker_symbol = ticker.upper()
        self.ticker_data = yf.Ticker(self.ticker_symbol.upper())
        self.info = self.ticker_data.info

        iv_dict = {}

        # Get stock price
        self._get_stock_price()

        try:
            # Get EPS
            self._get_eps()
        except:
            pass

        # financials = self.ticker_data.financials
        # for key, value in financials.items():
        #     print(f'{key}: {value}')

        try:
            self._get_growth()
        except:
            pass

        try:
            self._get_growth_secondary()
        except:
            pass

        # Force to break it if data not found
        if self.eps == 0:
            self.eps = None
        if self.growth_rate == 0:
            self.growth_rate = None

        intrinsic_value_data = self._calculate_intrinsic_value()

        if callout:
            self.print_callout(intrinsic_value_data)
        else:
            print(f'    {self.ticker_symbol}: {intrinsic_value_data[0]}')

        self.aggregate_total += float(intrinsic_value_data[0])

        return iv_dict.update({self.ticker_symbol: [self.value_difference, intrinsic_value_data[2]]})

    def print_callout(self, data_list):
        print(f'{self.ticker_symbol}: {data_list[1]}% @ ${data_list[2]} '
              f'for a rebate of ${data_list[3]}')

    def _get_eps(self):
        """
        Retrieves the current stock's EPS
        :return:
        """
        # Get EPS
        for key, value in self.info.items():
            # print(f'{key}: {value}')
            if key == 'forwardEps' and str(value) != 'None':
                # print(f'EPS (Forward): {value}')
                self.eps = value
                break
            if key == 'trailingEps':
                # print(f'EPS (Trailing): {value}')
                self.eps = value
                break

    def _get_stock_price(self):
        """
        Retrieves the current stock's price
        :return:
        """
        # Get stock price
        for key, value in self.info.items():
            # print(f'{key}: {value}')
            if key == 'currentPrice' and str(value) != 'None':
                # print(f'Current Price: {value}')
                self.current_price = value
                break

    def _get_growth_secondary(self):
        """
        Retrieves the current stock's secondary growth rate if growth rate not found
        :return:
        """
        # Another check for growth
        if self.growth_rate == 0:
            for key, value in self.info.items():
                if key == 'revenueGrowth' and str(value) != 'nan' and str(value) != 'None':
                    # print(f'Growth Rate (Revenue): {value}')
                    self.growth_rate = value

    def _get_growth(self):
        """
        Retrieves the current stock's growth rate
        :return:
        """
        # Get growth
        analysis = self.ticker_data.get_analysis(as_dict=True)
        for key, value in analysis.items():
            # print(f'{key}: {value}')
            if key == 'Growth':
                for key2, value2 in value.items():
                    if key2 == '0Q' and str(value2) != 'nan' and str(value2) != 'None':
                        # print(f'Growth Rate (0Q): {value2}')
                        self.growth_rate = value2
                        break
                    elif key2 == '+1Q' and str(value2) != 'nan' and str(value2) != 'None':
                        # print(f'Growth Rate (+1Q): {value2}')
                        self.growth_rate = value2
                        break
                    elif key2 == '0Y' and str(value2) != 'nan' and str(value2) != 'None':
                        # print(f'Growth Rate (0Y): {value2}')
                        self.growth_rate = value2
                        break
                    elif key2 == '+1Y' and str(value2) != 'nan' and str(value2) != 'None':
                        # print(f'Growth Rate (+1Y): {value2}')
                        self.growth_rate = value2
                        break
                    elif key2 == '+5Y' and str(value2) != 'nan' and str(value2) != 'None':
                        # print(f'Growth Rate (+5Y): {value2}')
                        self.growth_rate = value2
                        break

    def _calculate_intrinsic_value(self, supplied_intrinsic_value=0.0):
        """

        :return:
        """
        yield_of_current_bond = 3.8  # Find a way to fetch this

        if supplied_intrinsic_value == 0.0:
            # # Calculate Intrinsic Value (Original)
            # intrinsic_value = (eps * (8.5 + (2 * growth_rate)) * 4.4) / yield_of_current_bond
            # formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)

            # Calculate Intrinsic Value (Revised)
            intrinsic_value = (self.eps * (7 + self.growth_rate) * 4.4) / yield_of_current_bond

        formatted_intrinsic_value = "{:0.2f}".format(intrinsic_value)

        # Calculate value difference
        value_difference = self.current_price / intrinsic_value
        self.value_difference = value_difference * 100
        formatted_value_difference = "{:0.2f}".format(self.value_difference)

        # Acceptable buy price
        acceptable_buy_price = self.margin_of_safety * intrinsic_value
        formatted_acceptable_buy_price = "{:0.2f}".format(acceptable_buy_price)

        # Savings
        savings = float(self.current_price) - float(formatted_acceptable_buy_price)
        formatted_savings = "{:0.2f}".format(savings)

        return [formatted_intrinsic_value, formatted_value_difference, formatted_acceptable_buy_price,
                formatted_savings, acceptable_buy_price]


if __name__ == '__main__':
    run = SearchForStockData('iep')
    # run.print_stock_info()
