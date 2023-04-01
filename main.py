from stock_data.search_for_data_of_specific_stock_yfinance import SearchForStockData
from utilities.database_queries import Database


def run_bot():
    # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
    # Use a breakpoint in the code line below to debug your script.
    print(f'Welcome to the Trading Bot')
    while True:
        user_input = input('Select an option from the menu\n'
                           '1. See information about a specific stock\n'
                           '2. Create a personal ETF of stocks of your choice\n'
                           '3. Deposit money to your portfolio\n'
                           '4. Show portfolio\n')

        if user_input == '1':
            user_input1 = input('What stock would you like to see the information for?')
            SearchForStockData(user_input1)
            break
        elif user_input == '2':
            print('Not implemented yet')
        elif user_input == '3':
            print('Not implemented yet')
        elif user_input == '4':
            db = Database()
            db.print_formatted_portfolio()
            print('\n\n')
        else:
            print('Please enter a number from the menu')


if __name__ == '__main__':
    run_bot()
