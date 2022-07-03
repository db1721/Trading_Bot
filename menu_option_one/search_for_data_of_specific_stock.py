import quandl


class SearchForStockData:
    def __init__(self, stock_to_search):
        self.stock_to_search = stock_to_search

        print(f'Searching for {stock_to_search}....')

        # Get data via Quandl API
        data = quandl.get(f'WIKI/{stock_to_search}')
        # Summarize
        print(data.info())
