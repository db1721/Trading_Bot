from personal_portfolio.add_stock import AddStock
from utilities.database_queries import Database


class EditPortfolio:
    def __init__(self):
        """

        """
        pass

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
                'R - RETURN\n'
            )
            if user_input == '1':
                action = AddStock()
                action.add_stock()
                break
            elif user_input == '2':
                print('Not implemented yet')
                break
            elif user_input.upper() == 'R' or user_input.upper() == 'RETURN':
                break
