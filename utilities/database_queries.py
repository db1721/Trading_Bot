import csv
import os
import pandas

from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData
from utilities.all_utilities import AllUtilities


class Database:
    def __init__(self):
        self._util = AllUtilities()
        self._database_file_path = os.path.join(self._util.direct.get_database_directory(), 'portfolio.csv')
        self._fieldnames = ['ticker_symbol', 'portfolio_weight', 'quantity']
        self._portfolio = {}
        self._total_portfolio_weight = 0

    def write_portfolio(self, initial_portfolio_build):
        """

        :param initial_portfolio_build:
        :return:
        """
        with open(self._database_file_path, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._fieldnames)
            writer.writeheader()
            for stock in initial_portfolio_build:
                writer.writerow({'ticker_symbol': stock[0],
                                 'portfolio_weight': stock[1],
                                 'quantity': stock[2]})

    def _retrieve_portfolio(self):
        """
        Extracts data from portfolio
        :return:
        """
        with open(self._database_file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=self._fieldnames)
            line_count = 0
            for row in reader:
                # Skip headers
                if line_count == 0:
                    pass
                    line_count += 1
                else:
                    # Add data to portfolio dictionary
                    self._portfolio[row['ticker_symbol']] = {'portfolio_weight': row['portfolio_weight'],
                                                             'quantity': row['quantity']}
                line_count += 1
            # for key, value in self._portfolio.items():
            #     print(f'***{key}***')
            #     for key2, value2, in value.items():
            #         print(f'\t{key2}: {value2}')

    def get_portfolio(self):
        """
        Retrieve portfolio in dictionary format
        :return: portfolio in dictionary format
        """
        self._retrieve_portfolio()
        return self._portfolio

    def get_portfolio_weight(self):
        """

        :return:
        """
        pass

    def try_adding_stock(self, stock_to_add):
        """
        Trys adding the stock to the portfolio
        :param stock_to_add:
        :return:
        """
        stock_data = SearchForStockData(stock_to_add)
        if str(stock_data.current_price).isnumeric():
            print(stock_to_add)

    def print_formatted_portfolio(self):
        """
        Prints all the data in the database
        :return:
        """
        df = pandas.read_csv(self._database_file_path)
        print(df)
        print(f'{self._total_portfolio_weight}')


# run = Database()
# run.get_portfolio()
