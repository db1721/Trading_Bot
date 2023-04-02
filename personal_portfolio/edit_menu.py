from utilities.database_queries import Database


class EditPortfolio:
    def __init__(self):
        """

        """
        self._portfolio_query = Database()
        self.pd = self._portfolio_query.get_portfolio()

    def edit_menu(self):
        """
        Runs the edit menu to edit stocks in the portfolio
        :return:
        """
        print(f'Trading Bot - Edit Menu')
        while True:
            user_input = input(
                'Select an option from the menu\n'
                '1. Add Stock\n'
                '2. Remove Stock\n'
                '3. Edit Stock\n'
                '4. Show portfolio\n'
                '5. Edit portfolio\n'
            )
            if user_input == '1':
                self.add_stock()
                break
            elif user_input == '2':
                print('Not implemented yet')
                break

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
            if user_input in self.pd.keys():
                print(f'{user_input.upper()} already on portfolio')
                break
            else:
                try:
                    self._portfolio_query.try_adding_stock(user_input)
                    print(f'{user_input.upper()} added to Portfolio')
                    break
                # Checks if the stock exists
                except TypeError:
                    print(f'Unable to add {user_input.upper()} to Portfolio')

    # def _get_added_stock_
