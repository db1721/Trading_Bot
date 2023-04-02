import csv
import os
import pandas

from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData
from utilities.all_utilities import AllUtilities
from utilities.calculations.calculations import Calculations


class Database:
    def __init__(self):
        self._util = AllUtilities()
        self._database_file_path = os.path.join(self._util.direct.get_database_directory(), 'portfolio.csv')
        self._fieldnames = ['ticker_symbol', 'user_set_portfolio_weight', 'auto_balanced_portfolio_weight', 'quantity']
        self._portfolio = {}
        self._total_portfolio_weight = 0
        self._calculations = Calculations()

        self._retrieve_portfolio()

    def write_portfolio(self, initial_portfolio_build):
        """
        Writes portfolio to a csv file
        :param initial_portfolio_build:
        :return:
        """
        with open(self._database_file_path, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self._fieldnames)
            writer.writeheader()
            for stock in initial_portfolio_build:
                writer.writerow({'ticker_symbol': stock[0],
                                 'user_set_portfolio_weight': stock[1],
                                 'auto_balanced_portfolio_weight': stock[2],
                                 'quantity': stock[3]})

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
                    self._portfolio[row['ticker_symbol']] = {'user_set_portfolio_weight': row[
                        'user_set_portfolio_weight'],
                                                             'auto_balanced_portfolio_weight': row[
                                                                 'auto_balanced_portfolio_weight'],
                                                             'quantity': row['quantity']}
                line_count += 1

            # Keep for debugging
            # for key, value in self._portfolio.items():
            #     print(f'***{key}***')
            #     for key2, value2, in value.items():
            #         print(f'\t{key2}: {value2}')

    def get_portfolio(self):
        """
        Retrieve portfolio in dictionary format
        :return: portfolio in dictionary format
        """
        return self._portfolio

    def find_specific_stock_data_from_portfolio(self, stock, header):
        """
        Retrieves selected header data from portfolio
        :param stock:
        :param header:
        :return:
        """
        return self._portfolio[stock][header]

    def get_total_weight_of_current_portfolio(self):
        """
        Returns total weight of current portfolio
        :return: Total weight of current portfolio
        """
        total_weight = 0.0
        for key, value in self._portfolio.items():
            total_weight += float(self._portfolio[key]['user_set_portfolio_weight'])
        return total_weight

    def get_total_value_of_current_portfolio(self):
        """
        Returns total weight of current portfolio
        :return: Total weight of current portfolio
        """
        self._calculations.calculate_total_value_of_portfolio(self._portfolio)

    def print_formatted_portfolio(self):
        """
        Prints all the data in the database
        :return:
        """
        df = pandas.read_csv(self._database_file_path)
        print(df)
        print(f'{self._total_portfolio_weight}')


run = Database()
print(run.get_total_value_of_current_portfolio())
